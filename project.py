import pandas as pd
import csv
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import seaborn as sns

if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", famity="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False


class MyError(Exception):
    pass


# 시간대별 혼잡도 비교 그래프 그리기
# line plot


def comparebytime():

    df = pd.read_csv("서울교통공사_지하철혼잡도정보_20250331.csv", encoding="utf-8-sig")

    valid_station = df["출발역"].unique()
    print(valid_station)

    try:
        search = input("역을 검색해주세요: ")
        if search not in valid_station:
            raise MyError("존재하지 않는 역입니다")

        towhere = input("상/하선 선택: ")
        if towhere != "상선" and towhere != "하선":
            raise MyError("상선/하선 중에 선택하세요")

        # 1. 역 + 선 필터링
        station_towhere = df[(df["출발역"] == search) & (df["상하구분"] == towhere)]

        # 2. 시간대 열 추출
        time_columns = df.columns[5:]  # 0530 ~ 0030
        congestion = station_towhere[time_columns].iloc[0]  # 해당 row의 혼잡도

        # 3. 그래프

        plt.figure(figsize=(12, 5))
        plt.plot(time_columns, congestion, marker="o", color="skyblue")
        plt.title(f"{search} {towhere}선 - 시간대별 혼잡도")
        plt.xlabel("시간대")
        plt.ylabel("혼잡도 (%)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.axhspan(0, 34, facecolor="green", alpha=0.05)  # 여유
        plt.axhspan(35, 79, facecolor="yellow", alpha=0.05)  # 보통
        plt.axhspan(80, 99, facecolor="orange", alpha=0.05)  # 혼잡
        plt.axhspan(100, 119, facecolor="red", alpha=0.05)  # 매우 혼잡
        plt.axhspan(120, 149, facecolor="purple", alpha=0.05)  # 포화
        plt.axhspan(150, 200, facecolor="black", alpha=0.05)  # 초과혼잡

        plt.show()

    except MyError as e:
        print(f"Error: {e}")


def showtoplow15():

    df = pd.read_csv("서울교통공사_지하철혼잡도정보_20250331.csv", encoding="utf-8-sig")
    # print(df)

    # df.to_csv("subway_information.csv", index=False, encoding="utf-8-sig")

    # data2 = pd.read_csv("subway_information.csv", encoding="utf-8-sig")
    # data2.to_csv("subway_information.csv", index=False, encoding="utf-8-sig")

    df = pd.read_csv("서울교통공사_지하철혼잡도정보_20250331.csv", encoding="utf-8-sig")
    time_cols = df.columns[5:]
    df[time_cols] = df[time_cols].apply(pd.to_numeric, errors="coerce")
    df["행평균"] = df[time_cols].mean(axis=1)
    station_avg_series = df.groupby("출발역")["행평균"].mean()
    station_mean = station_avg_series.reset_index()
    station_mean.columns = ["출발역", "역평균혼잡도"]
    top15 = station_mean.sort_values("역평균혼잡도", ascending=False).head(15)
    bottom15 = station_mean.sort_values("역평균혼잡도", ascending=True).head(15)
    station_mean.columns = ["출발역", "역평균혼잡도"]

    mpl.rc("font", family="Malgun Gothic")
    mpl.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(12, 5))
    plt.bar(top15["출발역"], top15["역평균혼잡도"], color="pink")
    plt.title("평균 혼잡도 상위 15개 역")
    plt.ylabel("혼잡도 (%)")
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(bottom15["출발역"], bottom15["역평균혼잡도"], color="skyblue")
    plt.title("평균 혼잡도 하위 15개 역")
    plt.ylabel("혼잡도 (%)")
    plt.show()


def comparebyline():

    file_path = "서울교통공사_지하철혼잡도정보_20250331.csv"
    data_or = pd.read_csv(file_path, encoding="utf-8-sig")

    try:
        data = data_or[data_or["요일구분"] == "평일"].copy()
    except KeyError:
        print("'요일구분' 컬럼이 존재하지 않습니다.")
        exit()

    # 시간대 평균 열 생성
    try:
        시간대_구간 = {
            "05:30~08:30": [
                "5시30분",
                "6시00분",
                "6시30분",
                "7시00분",
                "7시30분",
                "8시00분",
                "8시30분",
            ],
            "08:31~11:30": [
                "9시00분",
                "9시30분",
                "10시00분",
                "10시30분",
                "11시00분",
                "11시30분",
            ],
            "11:31~14:30": [
                "12시00분",
                "12시30분",
                "13시00분",
                "13시30분",
                "14시00분",
                "14시30분",
            ],
            "14:31~17:30": [
                "15시00분",
                "15시30분",
                "16시00분",
                "16시30분",
                "17시00분",
                "17시30분",
            ],
            "17:31~20:30": [
                "18시00분",
                "18시30분",
                "19시00분",
                "19시30분",
                "20시00분",
                "20시30분",
            ],
            "20:31~23:30": [
                "21시00분",
                "21시30분",
                "22시00분",
                "22시30분",
                "23시00분",
                "23시30분",
            ],
            "23:31~00:30": ["00시00분", "00시30분"],
        }

        for 구간, 열목록 in 시간대_구간.items():
            for 열 in 열목록:
                if 열 not in data.columns:
                    raise KeyError(f"필요한 시간 컬럼이 없습니다: {열}")
            data[구간] = data[열목록].mean(axis=1)

    except Exception as e:
        print("시간대 평균 계산 오류:", e)
        exit()

    # 그룹화 및 시각화
    try:
        average = (
            data.groupby("호선")[list(시간대_구간.keys())]
            .mean()
            .reset_index()
            .melt(id_vars="호선", var_name="시간대", value_name="평균혼잡도")
        )

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=average, x="시간대", y="평균혼잡도", hue="호선", palette="pastel"
        )
        plt.title("호선별 3시간 구간 평균 혼잡도 비교")
        plt.ylabel("혼잡도 (%)")
        plt.xticks(rotation=45)
        plt.legend(title="호선")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("시각화 오류:", e)


try:
    choice = int(
        input("선택(1: 시간대별 추이 / 2: 평균 혼잡도 / 3: 호선별 혼잡도 비교): ")
    )

    if choice == 1:
        comparebytime()
    elif choice == 2:
        showtoplow15()
    elif choice == 3:
        comparebyline()
except:
    print("Error: 1,2,3 중 선택해주세요")
