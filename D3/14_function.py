# 매개변수
# def greet2(name, age = 20): # 선언 시 defalut값 설정 가능
#     print('안녕하세요')
#     print(f'저는 {name}입니다')
#     print(f'저는 {age} 살입니다\n')

# greet2('홍길동', 25)
# greet2(age = 18, name = '홍길동')

# return
# def calc(a,b):
#     result1 = a + b
#     result2 = a * b
#     return result1, result2

# print(type(calc(2,4)))

# 팩토리얼 함수
# def factirial1(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result

# print(factirial1(3))

# 재귀함수
# def factorial2(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial2(n - 1)

# print(factorial2(4))


# 가변인자
# 매개변수의 개수를 정확히 모를 때
# def add_all(*args):
#     print(sum(args))

# add_all(1,2,3,4,5)

# def print_all(**kwags):
#     for key, value in kwags.items():
#         print(f'key: {key}, value: {value}')

# print_all(name = '홍길동', age = 20)

# def show_all(title, *args, **kwargs):
#     print(f'title: {title}')
#     print(f'args: {args}')
#     print(f'kwagrs: {kwargs}')
    

# show_all('제목', 1,2,3,4, name = '홍길동', age = 20)


# 소문자로 이루어진 문자 리스트를 함수에 넣어서
# 대문자로 출력해주는 함수

# fruits = ['apple', 'banana', 'cherry']

# def upper_case(list):
#     for i in list:
#         print(i.upper())

# upper_case(fruits)

# 최대 최소 합계 평균 개수
numbers = [20, 39, 133, 556, 23, 16, 72, 123]

# def find_max(list):
#     max = list[0]
#     min = list[0]

#     for i in list:
#         if max <= i:
#             max = i
#         if min >= i:
#             min = i
    
#     print(f'최댓값: {max}, 최솟값: {min}')

# find_max(numbers)

# 숫자 리스트와 기준 숫자를 받아 그 이상만 합계, 평균 구하기

def larger_than(list, num):
    sum = 0
    cnt = 0
    for i in list:
        if i >= num:
            sum += i
            cnt += 1
    print(f'합계: {sum}, 평균: {sum / cnt}')

larger_than(numbers, 30)



