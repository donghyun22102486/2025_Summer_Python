# 반복문

# for i in range(5):
#     print(i)


# fruits = ['사과', '바나나', '포도']

# for index, fruits in enumerate(fruits):
#     print(f'index:{index} , fruit:', {fruits})


# for i in range(3):
#     for j in range(3):
#         print((f"i: {i}, j:{j}"))

#     print()

# # 구구딘
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f'{dan} x {i} = {dan * i}')
#     print()


# # break
# for i in range(5):
#     print(i)
#     if i == 3:
#         break

# # continue
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# 1 ~ 10까지 반복하는데 
# 짝수만 출력
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# # 사용자가 숫자를 입력하면
# # 그 숫자의 구구단 출력
# number = int(input('숫자를 입력하세요(1~9): '))

# for i in range(1,10):
#     print(f'{number} x {i} = {number * i}')


# # while
# i = 0

# while True:
#     print(i)
#     i += 1
#     if i >= 10:
#         break


# 대소문자
fruits = ['apple', 'banana', 'cherry']

# # 위 배열을 다 대문자로 출력하세요

# 배열 길이 len(fruits)
for i in range (len(fruits)):
    print(fruits[i].upper())

# for each
for fruit in fruits:
    print(fruit.upper())


