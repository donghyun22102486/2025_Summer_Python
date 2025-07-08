import pandas as pd

# Series: 1차원 배열, 리스트와 비슷, 인덱스가 있다
# DataFrame: 2차원 테이블 구조, 행+열로 구성


# scores = [88, 90, 67, 70]

# s = pd.Series(scores, index=["철수", "영희", "민수", "지수"])

# print(s)


data = {
    "이름": ["철수", "영희", "민수", None],
    "국어": [90, 70, None, 78],
    "영어": [80, None, 70, 86],
    "수학": [100, 98, 50, 68],
}

df = pd.DataFrame(data)

# # 결측치 개수 확인
# print(df.isnull().sum())

# # 결측치 채우기
# mean_kor = df["국어"].mean()
# df["국어"] = df["국어"].fillna(mean_kor)
# df["영어"] = df["영어"].fillna(" - ")
# df["이름"] = df["이름"].fillna("이름없음")
# print(df)

# # DataFrame 수정
# df["이름"] = df["이름"].replace("이름없음", "길동")
# print(df)


# 결측치 채우기 - students2.csv
# 수학: 평균
# 국어: 0점 처리
# 영어: '없음' 처리
df = pd.DataFrame(pd.read_csv("D7/students2.csv"))
math_mean = df["수학"].mean()
df["수학"] = df["수학"].fillna(math_mean)
df["국어"] = df["국어"].fillna(0)
df["영어"] = df["영어"].fillna("없음")
# print(df)

# 부정행위 학생 제외
df_clean = df[df["부정행위"] == False]
# print(df_clean)

# 출석일 기준 (170)
df2 = df_clean[df_clean["출석일"] >= 170]
# print(df2)

# 그룹핑
# '영어'에 '없음' 들어있어서 에러
# 이중 리스트 -> DF 자료형 유지 위해서
grouped = df2.groupby("학년")[["국어", "영어", "수학"]].mean()
print(grouped)

top_student = df2.groupby("학년")[["국어", "영어", "수학"]].max()
print(top_student)
