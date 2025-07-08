import csv
import pandas as pd

# csv 파일 읽어오기
df = pd.read_csv("D7/students2.csv", encoding="utf-8-sig")

# csv 파일 저장하기
# df.to_csv("D7/students2_export.csv", index=False, encoding="utf-8-sig")

# xlsx 파일 읽기
# df_excel = pd.read_excel("students2.xlsx")

# xlsx 파일 저장
# df_excel.to_excel("studenst2_export.xlsx", index=False, engine="openpyxl")
