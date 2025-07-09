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


def compareNaCl_eatingtype():

    exclude_codes = [
        "01",
        "02",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
    ]

    # 해당 코드 제거
    df_filtered = df[~df["식품대분류코드"].astype(str).isin(exclude_codes)]

    # 식사형태별 평균 나트륨 함량 계산
    avg_na_filtered = df_filtered.groupby("식사형태")["나트륨(mg)"].mean().reset_index()

    # 시각화
    plt.figure(figsize=(8, 5))
    sns.barplot(data=avg_na_filtered, x="식사형태", y="나트륨(mg)", palette="Set2")
    plt.title("식사형태별 평균 나트륨 함량 (mg)")
    plt.xlabel("식사형태")
    plt.ylabel("평균 나트륨 (mg)")
    plt.tight_layout()
    plt.show()


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


# compareNaCl_eatingtype()
show_foodratio_eatingtype()
