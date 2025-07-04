# class

# 객체 object
# 데이터와 기능을 담은 단위
# 걍 자바랑 똑같음 여긴

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f'{self.name}가 멍멍 짖습니다')


# dog1 = Dog('초코', 3)
# dog2 = Dog('인절미', 5)

# dog1.bark()
# dog2.bark()


class Student:
    def __init__(self, name, score, major):
        self.name = name
        self.score = score
        self.major = major

    def show_info(self):
        print(f"이름: {self.name}\n점수: {self.score}")

    def get_avg(self):
        tot = sum(self.score)
        avg = tot / len(self.score)
        print(f"평균: {avg:.2f}")  # f-string 사용 시 {x:.2f} 하면 둘째 자리까지 보여줌

    def get_major(self):
        print(f"전공: {self.major}")


jimin = Student("지민", [80, 50, 70], "컴공")
jimin.show_info()
jimin.get_avg()
jimin.get_major()

chulsoo = Student("철수", [60, 2, 10], "ITM")
chulsoo.show_info()
chulsoo.get_avg()
chulsoo.get_major()

