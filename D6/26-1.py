import pandas as pd

# csv 파일 읽기
df = pd.read_csv("D6/students.csv", encoding="utf-8-sig")
# print(df)

# csv 파일 저장
df.to_csv("D6/students_export.csv", index=False, encoding="utf-8-sig")

# excel 파일 읽기
df_excel = pd.read_excel("D6/students.xlsx")
# print(df_excel)

# excel 파일 저장
df_excel.to_excel("D6/students_export.xlsx", index=False, engine="openpyxl")
