import pandas as pd
import csv
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import seaborn as sns
import streamlit as st

if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", famity="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False


class MyError(Exception):
    pass


# 데이터 로드 및 결측치 0으로 일괄처리
df = pd.read_csv("전국통합식품영양성분정보_음식_표준데이터.csv", encoding="utf-8-sig")
df = df.fillna(0)
# print(df.isnull().sum())
# print(df.isna().sum())


def classify(source):

    source = str(source)

    if "가정식" in source:
        return "가정식"
    elif "외식" in source or "프랜차이즈" in source:
        return "외식"
    elif "급식" in source:
        return "급식"
    else:
        return "기타"


df["식사형태"] = df["식품기원명"].apply(classify)


# 식품 유형 분포 EDA
def show_foodratio_eatingtype():
    # 교차표 만들기 (count 기준)
    cross_tab = pd.crosstab(df["식사형태"], df["식품대분류명"])

    # 비율로 변환 (행 합 기준으로 정규화)
    cross_ratio = cross_tab.div(cross_tab.sum(axis=1), axis=0)

    # 보기 좋게 비율(%)로 변환
    cross_ratio_percent = (cross_ratio * 100).round(1)

    # stacked bar chart로 시각화
    cross_ratio_percent.T.plot(
        kind="barh", stacked=True, figsize=(5, 10), colormap="tab20"
    )
    plt.title("식사형태별 음식 대분류 구성비 (%)")
    plt.xlabel("비율 (%)")
    plt.ylabel("음식 대분류명")
    plt.yticks(rotation=0)
    plt.legend(title="식사형태")
    plt.tight_layout()
    plt.show()


# show_foodratio_eatingtype()


# 비교할 영양 성분들
nutrient_cols = [
    "에너지(kcal)",
    "수분(g)",
    "단백질(g)",
    "지방(g)",
    "회분(g)",
    "탄수화물(g)",
    "당류(g)",
    "식이섬유(g)",
    "칼슘(mg)",
    "철(mg)",
    "인(mg)",
    "칼륨(mg)",
    "나트륨(mg)",
    "비타민 A(μg RAE)",
    "레티놀(μg)",
    "베타카로틴(μg)",
    "티아민(mg)",
    "리보플라빈(mg)",
    "니아신(mg)",
    "비타민 C(mg)",
    "비타민 D(μg)",
    "콜레스테롤(mg)",
    "포화지방산(g)",
    "트랜스지방산(g)",
]

# 사용자 선택 UI
st.title("음식 대분류별 영양성분 비교")
selected_category = st.selectbox(
    "분석할 음식 대분류를 선택하세요", sorted(df["식품대분류명"].unique())
)
selected_nutrients = st.multiselect(
    "분석할 영양성분을 선택하세요",
    nutrient_cols,
    default=[
        "단백질(g)",
        "지방(g)",
        "탄수화물(g)",
    ],
)

# 필터링
filtered_df = df[df["식품대분류명"] == selected_category]

# 영양 성분 평균 계산
avg_nutrients = filtered_df.groupby("식사형태")[selected_nutrients].mean().reset_index()

# melt로 long-format 변환 (Seaborn용)
# 그래프로 만들기 좋게 길게 풀어 쓰기
melted = avg_nutrients.melt(id_vars="식사형태", var_name="영양성분", value_name="값")

st.title("전국 식품 영양성분 정보")

tab1, tab2 = st.tabs(["식사형태별 음식 대분류 구성비", "식사형태별 영양성분 평균 비교"])

# 시각화
with tab2:
    st.subheader(f"{selected_category} - 식사형태별 영양성분 평균 비교")

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(data=melted, x="영양성분", y="값", hue="식사형태", palette="Set2")
    plt.title(f"{selected_category} - 영양성분 평균값 (식사형태별)")
    plt.ylabel("값 (단위: kcal / g / mg)")
    plt.xlabel("영양성분")
    plt.tight_layout()
    st.pyplot(fig)

with tab1:
    # 교차표 만들기 (count 기준)
    cross_tab = pd.crosstab(df["식사형태"], df["식품대분류명"])

    # 비율로 변환 (행 합 기준으로 정규화)
    cross_ratio = cross_tab.div(cross_tab.sum(axis=1), axis=0)

    # 보기 좋게 비율(%)로 변환
    cross_ratio_percent = (cross_ratio * 100).round(1)

    fig, ax = plt.subplots(figsize=(8, 16))

    # stacked bar chart로 시각화
    cross_ratio_percent.T.plot(kind="barh", stacked=True, ax=ax, colormap="tab20")

    ax.set_title("식사형태별 음식 대분류 구성비 (%)")
    ax.set_xlabel("비율 (%)")
    ax.set_ylabel("음식 대분류명")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.legend(title="식사형태")
    plt.tight_layout()
    st.pyplot(fig)
