# 조건문 if

# 조건이 True 일 때 코드를 실행한다
# if, elif, else

# # 조건문 1
# age = 20

# if age >= 18:
#     print("성인입니다")
# else:
#     print("미성년자입니다")


# # 조건문2
# score = 83

# if score >= 90:
#     if score >= 97:
#         print("A+")
#     elif score >= 94:
#         print("A")
#     else:
#         print("A-")
# elif score >= 80:
#     if score >= 87:
#         print("B+")
#     elif score >= 84:
#         print("B")
#     else:
#         print("B-")
# elif score >= 70:
#     print("C")
# else:
#     print("F")


# # 논리연산자 활용
# is_student = True
# age = 20

# if is_student and age >= 20:
#     print("대학생입니다")

# # 리스트 활용
# fruits = ["사과", "바나나", "포도"]
# favorite = input("좋아하는 과일을 입력하세요: ")

# if favorite in fruits:
#     print(f"{favorite}는 과일목록에 있습니다")
# else:
#     print(f"{favorite}는 과일목록에 없습니다")


# # 숫자를 두 개 입력받아서 계산하기
# # 파이썬엔 double이 없어요~
# num1 = float(input("첫 번째 숫자: "))
# num2 = float(input("두 번째 숫자: "))
# operator = input("연산자를 입력하세요(=, -, *, /): ")

# if operator == "+":
#     print("더하기:", num1 + num2)
# elif operator == "-":
#     print("빼기:", num1 - num2)
# elif operator == "*":
#     print("곱하기:", num1 * num2)
# elif operator == "/":
#     print("나누기:", num1 / num2)


# 숫자를 하나 입력받아서
# 짝수인지 홀수인지
number = int(input('숫자를 입력해주세요: '))

if number % 2 == 1:
    print(f'{number}은 홀수입니다.')
else:
    print(f'{number}은 짝수입니다')    



