# 예외 처리

try:
    num1 = 10
    num2 = int(input("숫자를 입력하세요: "))
    print(num1 / num2)
except:
    print("올바른 숫자를 입력하세요.")
finally:
    print("프로그램이 종료됩니다.")
