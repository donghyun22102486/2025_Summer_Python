import pandas as pd
import csv
import json

import streamlit as st

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


def load_data():

    df = pd.read_csv("서울교통공사_지하철혼잡도정보_20250331.csv", encoding="utf-8-sig")
    df["출발역"] = df["출발역"].str.strip()
    df["상하구분"] = df["상하구분"].str.strip()
    return df


df = load_data()
time_columns = df.columns[5:]

st.title("지하철 혼잡도 분석")

tab1, tab2, tab3 = st.tabs(["시간대별 추이", "평균 혼잡도", "호선별 혼잡도 비교"])


with tab1:
    station = st.selectbox(
        "출발역 선택", sorted(df["출발역"].unique()), key="tab1_station"
    )
    direction = st.radio("상/하/내/외선 선택", ["상선", "하선", "내선", "외선"])

    subset = df[(df["출발역"] == station) & (df["상하구분"] == direction)]

    if not subset.empty:
        congestion = subset[time_columns].iloc[0]
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(
            time_columns,
            congestion,
            marker="o",
            color="skyblue",
            label=f"{station} {direction}",
        )
        ax.set_title(f"{station} {direction} - 시간대별 혼잡도")
        ax.set_xlabel("시간대")
        ax.set_ylabel("혼잡도 (%)")
        ax.set_xticks(range(len(time_columns)))
        ax.set_xticklabels(time_columns, rotation=45)
        ax.grid(True)

        ax.axhspan(0, 34, facecolor="green", alpha=0.05)
        ax.axhspan(35, 79, facecolor="yellow", alpha=0.05)
        ax.axhspan(80, 99, facecolor="orange", alpha=0.05)
        ax.axhspan(100, 119, facecolor="red", alpha=0.05)
        ax.axhspan(120, 149, facecolor="purple", alpha=0.05)
        ax.axhspan(150, 200, facecolor="black", alpha=0.05)

        st.pyplot(fig)
    else:
        st.warning("해당 조건에 맞는 데이터가 없습니다.")


with tab2:

    time_sorted = {
        "아침(06시~09시)": [
            "6시00분",
            "6시30분",
            "7시00분",
            "7시30분",
            "8시00분",
            "8시30분",
        ],
        "오전(09시~12시)": [
            "9시00분",
            "9시30분",
            "10시00분",
            "10시30분",
            "11시00분",
            "11시30분",
        ],
        "점심(12시~13시)": [
            "12시00분",
            "12시30분",
        ],
        "오후(13시~17시)": [
            "13시00분",
            "13시30분",
            "14시00분",
            "14시30분",
            "15시00분",
            "15시30분",
            "16시00분",
            "16시30분",
        ],
        "저녁(17시~20시)": [
            "17시00분",
            "17시30분",
            "18시00분",
            "18시30분",
            "19시00분",
            "19시30분",
            "20시00분",
        ],
        "야간(20시~(익)01시)": [
            "20시00분",
            "20시30분",
            "21시00분",
            "21시30분",
            "22시00분",
            "22시30분",
            "23시00분",
            "23시30분",
            "00시00분",
            "00시30분",
        ],
    }

    selected_day = st.selectbox("요일 선택", df["요일구분"].unique(), key="tab2_day")
    selected_times = st.selectbox(
        "시간대 선택", list(time_sorted.keys()), key="tab2_time"
    )

    selected_columns = time_sorted[selected_times]

    subset = df[df["요일구분"] == selected_day].copy()
    subset["선택시간 평균"] = subset[selected_columns].mean(axis=1)

    station_avg = subset.groupby("출발역")["선택시간 평균"].mean().reset_index()
    station_avg.columns = ["출발역", "역평균혼잡도"]

    top15 = station_avg.sort_values("역평균혼잡도", ascending=False).head(15)
    bottom15 = station_avg.sort_values("역평균혼잡도", ascending=True).head(15)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("혼잡도 상위 15개 역")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.bar(top15["출발역"], top15["역평균혼잡도"], color="pink")
        ax1.set_xticklabels(top15["출발역"], rotation=60)
        st.pyplot(fig1)

    with col2:
        st.subheader("혼잡도 하위 15개 역")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(bottom15["출발역"], bottom15["역평균혼잡도"], color="skyblue")
        ax2.set_xticklabels(bottom15["출발역"], rotation=60)
        st.pyplot(fig2)


with tab3:
    st.subheader("호선별 혼잡도 꺾은선 비교")

    one_hour_columns = [col for col in df.columns if "시" in col and "30분" not in col]

    # 사용자 선택
    selected_day = st.selectbox("요일 선택", df["요일구분"].unique(), key="tab3_day")
    selected_lines = st.multiselect(
        "호선 선택", sorted(df["호선"].unique()), default=["2호선", "3호선"]
    )

    if selected_lines:
        # 데이터 필터링
        filtered = df[
            (df["요일구분"] == selected_day) & (df["호선"].isin(selected_lines))
        ].copy()

        # 호선별 시간대 평균 계산
        avg_by_line = filtered.groupby("호선")[one_hour_columns].mean().transpose()

        # 시각화
        fig, ax = plt.subplots(figsize=(12, 5))
        for line in selected_lines:
            ax.plot(one_hour_columns, avg_by_line[line], marker="o", label=f"{line}")

        ax.set_title(f"{selected_day} - 호선별 시간대별 평균 혼잡도")
        ax.set_xlabel("시간대")
        ax.set_ylabel("혼잡도 (%)")
        ax.set_xticks(range(len(one_hour_columns)))
        ax.set_xticklabels(one_hour_columns, rotation=45)
        ax.legend(title="호선")
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.info("비교할 호선을 하나 이상 선택하세요.")


# with tab3:
#     시간대_구간 = {
#         "05:30~08:30": [
#             "5시30분",
#             "6시00분",
#             "6시30분",
#             "7시00분",
#             "7시30분",
#             "8시00분",
#             "8시30분",
#         ],
#         "08:31~11:30": [
#             "9시00분",
#             "9시30분",
#             "10시00분",
#             "10시30분",
#             "11시00분",
#             "11시30분",
#         ],
#         "11:31~14:30": [
#             "12시00분",
#             "12시30분",
#             "13시00분",
#             "13시30분",
#             "14시00분",
#             "14시30분",
#         ],
#         "14:31~17:30": [
#             "15시00분",
#             "15시30분",
#             "16시00분",
#             "16시30분",
#             "17시00분",
#             "17시30분",
#         ],
#         "17:31~20:30": [
#             "18시00분",
#             "18시30분",
#             "19시00분",
#             "19시30분",
#             "20시00분",
#             "20시30분",
#         ],
#         "20:31~23:30": [
#             "21시00분",
#             "21시30분",
#             "22시00분",
#             "22시30분",
#             "23시00분",
#             "23시30분",
#         ],
#         "23:31~00:30": ["00시00분", "00시30분"],
#     }

#     for 구간, 열목록 in 시간대_구간.items():
#         df[구간] = df[열목록].mean(axis=1)

#     avg = df.groupby("호선")[list(시간대_구간.keys())].mean().reset_index()
#     melt_df = avg.melt(id_vars="호선", var_name="시간대", value_name="평균혼잡도")

#     fig3 = plt.figure(figsize=(12, 6))
#     sns.barplot(data=melt_df, x="시간대", y="평균혼잡도", hue="호선", palette="pastel")
#     plt.xticks(rotation=45)
#     plt.title("호선별 시간구간 평균 혼잡도 비교")
#     plt.tight_layout()
#     st.pyplot(fig3)


# fast api
# 강사님
