students = [
    {"name": "철수", "score": 82},
    {"name": "영희", "score": 64},
    {"name": "길동", "score": 73},
    {"name": "재석", "score": 95},
]


def print_students():
    print("\n전체 학생 목록")
    for student in students:
        print(f'{student["name"]} - {student["score"]}')


def get_average():
    sum = 0
    for student in students:
        sum += student["score"]
    avg = sum / len(students)
    print(f"평균 점수: {avg}점")


def get_top_student():
    # max = students[0]["score"]
    # for student in students:
    #     if max <= student["score"]:
    #         max = student["score"]
    # for student in students:
    #     if student["score"] == max:
    #         print(f'최고점 학생: {student["name"]} - {student["score"]}점')
    top_student = students[0]
    for student in students:
        if student["score"] >= top_student["score"]:
            top_student = student
    print(f'최고점 학생: {top_student["name"]} - {top_student["score"]}점')
    


def get_lowest_student():
    min = students[0]["score"]
    for student in students:
        if min >= student["score"]:
            min = student["score"]
    for student in students:
        if student["score"] == min:
            print(f'최하점 학생: {student["name"]} - {student["score"]}점')


def filter_high_score():
    num = int(input('기준 점수: '))
    for student in students:
        if student["score"] < num:
            print(f'{num}점 미만 학생: {student["name"]} - {student["score"]}점')


def add_student():
    name_input = input("이름: ")
    score_input = int(input("점수: "))
    students.append({"name": name_input, "score": score_input})
    print(f"업데이트된 학생 목록:")
    for student in students:
        print(f'{student["name"]} - {student["score"]}')


# 프로그램 실행
while True:
    print("\n***** 학생 성적 관리 프로그램 *****")
    print("1. 전체 학생 목록 출력")
    print("2. 평균 점수 출력")
    print("3. 최고 점수 학생 출력")
    print("4. 최저 점수 학생 출력")
    print("5. 기준 점수 미만 학생 출력")
    print("6. 학생 추가")
    print("0. 프로그램 종료")

    choice = int(input("\n메뉴 번호를 선택하세요: "))
    
    if choice == 1:
        print_students()
    elif choice == 2:
        get_average()
    elif choice == 3:
        get_top_student()
    elif choice == 4:
        get_lowest_student()
    elif choice == 5:
        filter_high_score()
    elif choice == 6:
        add_student()
    elif choice == 0:
        print('프로그램 종료')
        break
    else:
        print('다시 입력해주세요')