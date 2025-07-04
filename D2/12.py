# 삽입 정렬

# 리스트를 앞에서부터 하나씩 읽으면서
# 그 값을 정렬된 구간에 맞게 왼쪽에 삽입

# 정렬된 구간을 유지하면서
# 새로운 값을 삽입할 공간을 찾는 방식
# 그래서 역순으로 검사하는게 빠름

numbers = [5, 3, 8, 4, 2]
# 3, 5, 8, 4, 2
# 3, 4, 5, 8, 2
# 2, 3, 4, 5, 8

n = len(numbers)

for i in range(1, n):
    key = numbers[i]
    
    for j in range(i - 1, -2, -1):
    
        if j == -1 or numbers[j] <= key:
            numbers[j + 1] = key
            break
    
        else:
            numbers[j + 1] = numbers[j]

print(numbers)
