# 최대값, 최소값, 합계, 평균, 개수

numbers = [20, 39, 133, 556, 23, 16, 72, 123]

# max = numbers[0]
# min = numbers[0]

# for i in numbers:
#     if max <= i:
#         max = i
#     if min >= i:
#         min = i

# max = max(numbers)
# min = min(numbers)

# print(f'최대값: {max}')
# print(f'최솟값: {min}')

# sum = 0

# for number in numbers:
#     sum += number

# print(f'합계: {sum}')

# avg = sum / len(numbers)
# print(f'평균: {avg}')

# 30 이상만 합계, 평균
# cnt
sum = 0
cnt = 0

for number in numbers:
    if number >= 30:
        cnt += 1
        sum += number

avg = sum / cnt

# 새로운 list
num30 = []

for number in numbers:
    if number >= 30:
        num30.append(number)

sum = sum(num30)
avg = sum / len(num30)

print(f"합계: {sum}")
print(f"평균: {avg}")
