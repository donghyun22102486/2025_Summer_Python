class Student:
    def __init__(self, name, age, major, scores):
        self.name = name
        self.age = age
        self.major = major
        self.scores = scores


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        print("\n***** 전체 학생 출력 *****")
        for s in self.students:
            print(f"이름: {s.name}, 나이: {s.age}, 전공: {s.major}\n점수: {s.scores}\n")

    def avg_score(self):
        print("\n***** 과목별 평균 점수 출력 *****")

        for i in range(len(self.students[0].scores)):
            tot = 0

            for s in self.students:
                for class_name, score in s.scores[i].items():
                    tot += int(score)

            avg = tot / len(self.students)
            print(f"과목: {class_name}, 평균: {avg:.2f}")

    def top_score(self):
        print("\n***** 과목별 최고점 학생 *****")

        for i in range(len(self.students[0].scores)):
            top_student = self.students[0]

            for s in self.students:
                for class_name, score in s.scores[i].items():
                    # 클래스.필드.items() > dict_veiw[] 라는 자료형 > list로 받아서 인덱스로 접근해야 자료형 이쁨
                    # 전처리 가능할 경우 클래스 생성자에서 그냥
                    # [{}, {}] 구조를 [{, , }] 로 변환하면 더 편함
                    if list(top_student.scores[i].values())[0] <= score:
                        top_student = s

            print(
                f"<{class_name}> 이름: {top_student.name} / 점수: {list(top_student.scores[i].values())[0]}"
            )

    def better_than(self):
        for i in range(len(self.students[0].scores)):
            cnt = 0
            standard = int(
                input(
                    f"\n{list(self.students[0].scores[i].keys())[0]} 기준 점수를 입력하세요: "
                )
            )
            print(
                f"\n{list(self.students[0].scores[i].keys())[0]} 과목 {standard}점 이상 학생 목록:"
            )

            for s in self.students:
                if list(s.scores[i].values())[0] >= standard:
                    print(f"이름: {s.name} / 점수: {list(s.scores[i].values())[0]}점")
                    cnt += 1
            if cnt == 0:
                print(f"{standard}점 이상인 학생이 없습니다.")


manager = StudentManager()

manager.add_student(Student("철수", 20, "ITM", [{"영어": 60}, {"파이썬": 100}]))
manager.add_student(Student("영희", 20, "ITM", [{"영어": 80}, {"파이썬": 68}]))
manager.add_student(Student("민수", 21, "컴공", [{"영어": 50}, {"파이썬": 78}]))
manager.add_student(Student("민지", 21, "전자", [{"영어": 89}, {"파이썬": 95}]))
manager.add_student(Student("재석", 22, "경영", [{"영어": 69}, {"파이썬": 75}]))
manager.add_student(Student("길동", 22, "컴공", [{"영어": 68}, {"파이썬": 88}]))


while True:
    try:
        print("\n1. 전체 학생 목록")
        print("2. 과목별 평균 점수")
        print("3. 과목별 최고 점수")
        print("4. 기준 점수 이상 학생")
        print("0. 프로그램 종료")

        choice = int(input("메뉴 번호 선택: "))

        if choice == 1:
            manager.show_all_students()

        elif choice == 2:
            manager.avg_score()

        elif choice == 3:
            manager.top_score()

        elif choice == 4:
            manager.better_than()

        elif choice == 0:
            print("프로그램을 종료합니다.")
            break
    except:
        print("올바른 번호를 입력하세요")
