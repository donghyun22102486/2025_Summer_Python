# 문자열
name = "철수"
print(name + " 안녕")
print(name, "안녕")

# 여러 줄로 이루어진 문자열
text1 = """
철수야
안녕
반가워
"""
print(text1)

text2 = """
철수야
안녕
반가워
"""
print(text2)


last_name = "홍"
first_name = "길동"
full_name = last_name + first_name
print(full_name)

# f string
print(f"나는 {last_name} {first_name} 이야")

# 문자열 길이
text3 = "안녕하세요 반가워요"
print("문자열 길이:", len(text3))

# 문자열 인덱싱
print("첫 번째 문자: ", text3[0])
print("마지막 문자: ", text3[-1])

# 슬라이싱
print("처음 6글자:", text3[:6])
print("7번째부터 끝까지:", text3[7:])

# 거꾸로 출력
print("거꾸로 출력:", text3[::-1])

# 대소문자
text4 = "Hello"
print("대문자로:", text4.upper())
print("대문자로:", text4.lower())

# 단어 수 세기
print("단어 수 세기:", text3.count("요"))

# 시작하는 단어 찾기
print('"안녕"으로 시작하나요?', text3.startswith("안녕"))

text5 = "   hello   "

# 공백 제거
print('공백 포함:', text5)
print('공백 제거:', text5.strip())

# 문자열 포맷팅
name = '홍길동'
age = 25

# 1. % 방식
print('제 이름은 %s이고, 나이는 %d살입니다.' %(name, age))

# 2. format{} 방식
print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))

# 3. f -string 방식 - 이걸 제일 많이쓰긴 함
print(f'제 이름은 {name}이고, 나이는 {age}살입니다.')

# 이스케이프 문자
print('줄바꿈\n다음 줄입니다')
print('탭\t탭입니다')
print('백슬래시: \\') 

# 입력받기
name = input('이름을 입력하세요: ')
print(f'입력한 이름: {name}')




