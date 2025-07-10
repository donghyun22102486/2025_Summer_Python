# D1

## 기초문법

자료형, f-string, 논리연산자, 리스트 인덱싱/슬라이싱, 정렬, 딕셔너리, 조건문

# D2

## 기초문법

반복문, 정렬 알고리즘, 함수 기초

# D3

## 기초문법

함수, 파일 입출력, 예외처리, 중첩 리스트/딕셔너리

## 실습

학생 성적 출력 프로그램

# D4

클래스, 모듈화, 라이브러리 사용법

# D5

## API 기초

API 연결, dotenv, 예외처리 응용, tabulate

## 실습

미세먼지 농도 api

# D6

## API 실습

Google AI Studio, Google workspace 이용한 Gemini API 연결

## Data 처리 기초

csv 파일 읽고 쓰기, json 파일로 변환, Pandas 기초<br>
공공데이터포털 - 서울교통공사\_지하역사\_공기질\_측정\_정보\_20240625.csv

# D7

## Data 처리 기초

Pandas 기초: 비교연산자, 그룹핑

## Data 시각화

matplotlib - 데이터 시각화: 그래프

## 팀 프로젝트

공공데이터포털 - 서울 지하철 혼잡도 데이터<br>
역, 혼잡도 평균, 호선 별 데이터 시각화

# D8

## seaborn 기초

데이터 시각화

## 팀 프로젝트

streamlit 사용해 웹으로 구현<br>
fast api ?

## 프로젝트 2

전국통합식품영양성분정보*음식*표준데이터.csv<br>
1차 EDA

# D9

## streamlit

streamlit 기초

## 프로젝트 2

1. 식사형태별 음식 대분류 구성비 탭 추가<br>
2. 식사형태별 영양성분 선택 후 비교 탭 추가

## Fast API

1. 디렉터리 구조

```
datasets/
├── 전국통합식품영양성분정보_음식_표준데이터.csv
foodinfo/
├── backend/                                    ← FastAPI 백엔드
│   ├── project3.py                             ← FastAPI 실행 파일 (app = FastAPI())
│
├── frontend/                                   ← React 프론트엔드 (npx create-react-app = npm으로 만든 React 프로젝트)
│   ├── package.json
│   ├── node_modules/
│   ├── public/
│   └── src/
│       └── App.js                              ← 직접 편집한 React 화면
```

2. frontend: React 생성 및 라이브러리 설치

```
- npx create-react-app .                        ← 현재 디렉터리에 React 프로젝트 생성
- npm install axios chart.js react-chartjs-2    ← 해당 프로젝트에 필요한 라이브러리 설치
```

3. 실행 방법

```
# 백엔드 실행
cd backend
python -m uvicorn project3:app --reload         ← 백엔드 fast api 실행

# 프론트엔드 실행
cd frontend
npm start                                       ← 프론트엔드 React 실행

```
