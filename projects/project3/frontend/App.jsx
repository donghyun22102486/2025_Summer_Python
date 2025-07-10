import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Legend,
  Tooltip,
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Legend, Tooltip);

function App() {
  const [categories, setCategories] = useState([]);
  const [nutrients, setNutrients] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [selectedNutrients, setSelectedNutrients] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/categories")
      .then((res) => setCategories(res.data));
    axios
      .get("http://localhost:8000/nutrients")
      .then((res) => setNutrients(res.data));
  }, []);

  const analyze = () => {
    axios
      .post("http://localhost:8000/analyze", {
        category: selectedCategory,
        nutrients: selectedNutrients,
      })
      .then((res) => setData(res.data));
  };

  const chartData = {
    labels: selectedNutrients,
    datasets: ["가정식", "외식", "급식"].map((type) => ({
      label: type,
      data: selectedNutrients.map((n) => {
        const row = data.find((d) => d["식사형태"] === type);
        return row ? row[n] : 0;
      }),
    })),
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h2>🍱 식사형태별 영양성분 비교</h2>

      <div>
        <label>대분류 선택: </label>
        <select onChange={(e) => setSelectedCategory(e.target.value)}>
          <option value="">-- 대분류 선택 --</option>
          {categories.map((c) => (
            <option key={c} value={c}>
              {c}
            </option>
          ))}
        </select>
      </div>

      <div style={{ marginTop: "10px" }}>
        <label>비교할 영양성분 선택:</label>
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "8px",
            marginTop: "5px",
          }}
        >
          {nutrients.map((n) => (
            <label key={n}>
              <input
                type="checkbox"
                value={n}
                onChange={(e) => {
                  const checked = e.target.checked;
                  setSelectedNutrients((prev) =>
                    checked ? [...prev, n] : prev.filter((x) => x !== n)
                  );
                }}
              />
              {n}
            </label>
          ))}
        </div>
      </div>

      <button onClick={analyze} style={{ marginTop: "15px" }}>
        분석하기
      </button>

      {data.length > 0 && (
        <div style={{ marginTop: "30px" }}>
          <Bar data={chartData} />
        </div>
      )}
    </div>
  );
}

export default App;
