# 버블 정렬

# 옆에 있는 값과 비교 -> 큰 수를 오른쪽으로 옮긴다

numbers = [5, 3, 4, 1]
# 3, 4, 1, 5
# 3, 1, 4, 5
# 1, 3, 4 ,5

n = len(numbers)

# 전체 정렬을 위한 n-1번 반복

for i in range(n - 1):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # a = numbers[j]
            # numbers[j] = numbers[j + 1]
            # numbers[j + 1] = a
            numbers[j], numbers[j+1] = numbers[j + 1], numbers[j] # 역시 파이썬
            print(f'{i+1} 회전 {j}번째 비교 후: {numbers}')


