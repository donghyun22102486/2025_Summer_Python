import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", famity="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False


# 막대그래프
# fruits = ["사과", "바나나", "포도", "딸기"]
# sales = [100, 80, 60, 40]

# plt.bar(fruits, sales, color="skyblue")
# plt.title("과일별 판매량")
# plt.xlabel("과일 종류")
# plt.ylabel("판매 개수")
# plt.show()


# 여러 개 그래프
# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 4, 6, 8, 10]

# plt.plot(x, y1, label="제곱")
# plt.plot(x, y2, label="2의 배수")
# plt.legend()
# plt.title("두 개의 선 그래프")
# plt.show()


x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 4]

# plt.plot(x, y, linestyle=":", color="green", marker="s", label="데이터 A")
# plt.title("선 스타일")
# plt.xlabel("X값")
# plt.xlabel("Y값")
# plt.legend()
# plt.grid(True)
# plt.show()

# 산점도
# plt.scatter(x, y, linestyle=":", color="green", s=500)
# plt.title("산점도")
# plt.xlabel("X값")
# plt.xlabel("Y값")
# plt.legend()
# plt.grid(True)
# plt.show()

# 히스토그램
import numpy as np

# data = np.random.randn(1000)

# plt.hist(data, bins=30, color="skyblue", edgecolor="black")
# plt.title("히스토그램")
# plt.xlabel("값의 구간")
# plt.xlabel("빈도수")
# plt.legend()
# plt.grid(True)
# plt.show()

# 파이 차트
# labels = ["python", "java", "C++"]
# sizes = [40, 30, 20]
# colors = ["gold", "yellowgreen", "lightcoral"]

# plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
# plt.title("언어 사용 비율")
# plt.axis("equal")
# plt.show()
