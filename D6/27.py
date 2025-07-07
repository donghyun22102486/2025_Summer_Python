import pandas as pd

data = {
    "이름": ["철수", "영희", "민수", "철수", None],
    "국어": [90, 85, None, 90, 70],
    "영어": [95, None, 88, 46, 60],
    "수학": [99, 100, 34, 67, 90],
}

# Series: 1차원 배열, 리스트와 배수, 인덱스가 있다
# DataFrame: 2차원 테이블 구조, 행+열 로 구성

# scores = pd.Series([88, 20, 100, 50], index=["철수", "영희", "민수", "지수"])
# print(scores)

# 딕셔너리 -> DataFrame
df = pd.DataFrame(data)
# print(df.head())  # 앞의 5개 출력
# print(df.tail())  # 뒤의 5개 출력
# print(df.shape)  # 행 열 출력
# print(df.columns)  # 컬럼명 확인
# print(df.describe())  # 통계 요약 정보

# 결측치 확인
# print(df.isnull())

# 결측치 채우기
mean_kor = df["국어"].mean()
# print(mean_kor)
df["국어"] = df["국어"].fillna(mean_kor)
df["영어"] = df["영어"].fillna("없음")
df["이름"] = df["이름"].fillna("이름없음")
print(df)
