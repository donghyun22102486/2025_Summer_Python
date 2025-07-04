# Python3 샘플 코드 #


import requests
from dotenv import load_dotenv
import os

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

# api_key = "tXR1Vgo7BqnWSTAVWjtiRx7FtWrGQrbjaTR2I5gTNGbqgvxfPJh1tz/dI7n8O0xjqMDjUKDCS6i/Q29q+v9hTg=="
# "tXR1Vgo7BqnWSTAVWjtiRx7FtWrGQrbjaTR2I5gTNGbqgvxfPJh1tz%2FdI7n8O0xjqMDjUKDCS6i%2FQ29q%2Bv9hTg%3D%3D"

# 민감한 정보는 dotenv 이용해서 따로 저장
# .env 파일 로드
load_dotenv()

# API키 불러오기
api_key = os.getenv("API_KEY")


# params = {
#     "serviceKey": api_key,
#     "returnType": "json",
#     "numOfRows": "100",
#     "pageNo": "1",
#     "sidoName": "서울",
#     "ver": "1.0",
#     # "searchDate": "2020-11-14",
#     # "InformCode": "PM10",
# }

### 1

# response = requests.get(url, params=params)

# # .json() --> 받아온 json() 데이터를 딕셔너리로 파싱
# # print(response.json())

# items = response.json()["response"]["body"]["items"]

# # 보기 예쁘게
# # for item in items:
# #     station = item["stationName"]
# #     pm10 = item["pm10Value"]
# #     pm25 = item["pm25Value"]

# #     print(f"{station}: PM10: {pm10} | PM25: {pm25}")


# # 내가 원하는 도시 이름을 입력하면 가져오기
# # 이상한 데이터 예외처리
# try:
#     input = input("도시 이름을 입력하세요: ")

#     for item in items:
#         station = item["stationName"]
#         pm10 = item["pm10Value"]
#         pm25 = item["pm25Value"]

#         if station == input:
#             print(f"{station}: PM10: {pm10} | PM25: {pm25}")
#             found = True

#     # if else 로 바로 예외처리하면
#     # 첫 경우 검색하자마자 바로 예외 발생
#     # boolean 사용하기
#     if found == False:
#         raise

# except:
#     print(f"{input}은 검색 가능한 도시가 아닙니다")


### 2
# 요청 전에 미리 걸러서 요청하기 ?
# 1. station 리스트 하드코딩
# 2. 미리 요청해서 리스트로 저장

valid_sidoName = [
    "전국",
    "서울",
    "부산",
    "대구",
    "인천",
    "광주",
    "대전",
    "울산",
    "경기",
    "강원",
    "충북",
    "충남",
    "전북",
    "전남",
    "경북",
    "경남",
    "제주",
    "세종",
]

# 내가 원하는 도시 이름을 입력하면 가져오기
# 이상한 데이터 예외처리

# 1. 아래 내용 추가로 출력하기
# 아황산가스, 일산화탄소, 오존, 일산화질소 농도

# 2. pm10 농도에 따라서 미세먼지 좋은, 보통, 나쁨 알려주기


class MyError(Exception):
    pass


try:
    input_sidoName = input("시/도 이름을 입력하세요: ")

    if input_sidoName in valid_sidoName:
        found = True

        if found == True:

            params = {
                "serviceKey": api_key,
                "returnType": "json",
                "numOfRows": "100",
                "pageNo": "1",
                "sidoName": input_sidoName,
                "ver": "1.0",
            }

            response = requests.get(url, params=params)
            items = response.json()["response"]["body"]["items"]

            for item in items:
                station = item["stationName"]
                pm10 = int(item["pm10Value"])
                pm25 = item["pm25Value"]
                so2 = item["so2Value"]
                co = item["coValue"]
                o3 = item["o3Value"]
                no2 = item["no2Value"]

                ## 홍릉로 다음에 결측치 있어서 에러
                if pm10 <= 30:
                    print(
                        f"{station} :  PM10: {pm10} | PM25: {pm25} | SO2: {so2} | CO: {co} | O3: {o3} | NO2{no2} | 미세먼지 좋음"
                    )
                elif pm10 <= 80:
                    print(
                        f"{station} :  PM10: {pm10} | PM25: {pm25} | SO2: {so2} | CO: {co} | O3: {o3} | NO2{no2} | 미세먼지 보통"
                    )
                elif pm10 <= 150:
                    print(
                        f"{station} :  PM10: {pm10} | PM25: {pm25} | SO2: {so2} | CO: {co} | O3: {o3} | NO2{no2} | 미세먼지 나쁨"
                    )
                else:
                    print(
                        f"{station} :  PM10: {pm10} | PM25: {pm25} | SO2: {so2} | CO: {co} | O3: {o3} | NO2{no2} | 미세먼지 매우 나쁨"
                    )

        else:
            raise MyError("검색 가능한 시/도가 아닙니다.")

except MyError as e:
    print(f"{input_sidoName}은 {e}")
