import csv

# csv 파일 저장하기
students = [
    {"name": "홍길동", "score": 90},
    {"name": "박민수", "score": 80},
    {"name": "김철수", "score": 70},
    {"name": "이영희", "score": 60},
]


# 함수로 이용하는게 편함
def makecsv(file):
    # csv 파일 저장하기
    with open(file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(students)

    print("csv 저장 완료")


# makecsv("D6/students.csv")


def csvreader(file):
    with open(file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(row)


# csvreader("D6/students.csv")


import json


# json 파일 저장하기
def makejson(file):
    with open(file, "w", encoding="utf-8-sig") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    print("json 저장 완료")


# makejson("D6/students.json")


# json 파일 읽기
def readjson(file):
    with open(file, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    print(data)


# readjson("D6/students.json")


# 서울교통공사_지하역사_공기질_측정_정보_20240625
# 읽고 print()로 출력하고
# json으로 만들고
# json으로 출력


with open(
    "D6/서울교통공사_지하역사_공기질_측정_정보_20240625.csv", "r", encoding="utf-8-sig"
) as f:
    reader = csv.DictReader(f)

    data = []
    for row in reader:
        data.append(row)
        # print(row)

    # 리스트로 한번에
    # data = list(reader)


with open(
    "D6/서울교통공사_지하역사_공기질_측정_정보_20240625.json", "w", encoding="utf-8-sig"
) as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
