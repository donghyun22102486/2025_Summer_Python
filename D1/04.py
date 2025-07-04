# 리스트 list
fruits = ["사과", "바나나", "포도"]
print(fruits)

numbers = [1, 2, 3, 4, 5]
print(numbers)

# 리스트 인덱싱
print("첫 번째 과일:", fruits[0])
print("마지막 과일:", fruits[-1])

# 슬라이싱
print("1부터 4까지:", numbers[:4])

# 데이터 추가1
fruits.append("망고")
print(fruits)

# 데이터 추가2
fruits.insert(1, "오렌지")
print(fruits)

# 데이터 수정
fruits[2] = "키위"
print(fruits)

# 데이터 삭제
fruits.pop()
print(fruits)

fruits.remove("키위")
print(fruits)

# 인덱스 찾기
print('"오렌지"의 인덱스:', fruits.index("오렌지"))

fruits.append("사과")
print(fruits)
print('"사과"의 개수:', fruits.count("사과"))

# 정렬
fruits.sort()
print("정렬:", fruits)

fruits.reverse()
print("역순:", fruits)

text = "python, java, C++"
languages = text.split(",")
print(languages)

words = ['hello', '안녕하세요', '반가워요']
print(words)

sentence = " ".join(words)
print(sentence)


