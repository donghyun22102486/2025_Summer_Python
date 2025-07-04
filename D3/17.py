# 중첩 리스트, 딕셔너리

students = [
    {"name": "철수", "score": 82},
    {"name": "영희", "score": 64},
    {"name": "길동", "score": 73},
    {"name": "재석", "score": 95},
]

# 70점 이상인 학생 이름과 점수 출력

for student in students:
    if student["score"] >= 70:
        print(f'이름: {student["name"]}, 점수: {student["score"]}')



# classroom = {"A반": ["철수", "영희"], "B반": ["길동", "재석"]}

