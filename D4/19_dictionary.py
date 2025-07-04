# students = [
#     {"name": "철수", "score": 91, "attendance": "양호"},
#     {"name": "영희", "score": 87, "attendance": "불량"},
#     {"name": "민수", "score": 94, "attendance": "양호"},
# ]

# # 점수 90 이상, 출결 양호인 학생 출력
# for student in students:
#     if student["score"] >= 90 and student["attandence"] == "양호":
#         print(f'이름: {student["name"]}, 점수: {student["score"]}, 출결: {student["attendance"]}')

classrooms = {
    "1반": ["민수", "하늘", "가영"],
    "2반": ["철수", "지민"],
    "3반": ["영희", "하늘"],
    "4반": ["지민", "하늘", "슬기"]
}

# 지민이 포함된 반 이름 찾기
for class_name, students in classrooms.items():
    if "지민" in students:
        print(class_name)

# 각 순회마다 key를 앞의 변수, value를 뒤의 변수에 저장
# classrooms.items() --> classrooms 딕셔너리 안에 있는 값을
# (key, value)의 튜플로 반환
# for a in dict.items(): 로 하면 a = ("A", "B") 이렇게 튜플로 저장
# 변수 두 개 써주면 자동 언패킹으로 a = "A", b = "B" 이렇게 들어감




