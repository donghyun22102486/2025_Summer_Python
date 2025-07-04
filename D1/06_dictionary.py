# Dictionary
# 오브젝트
# 키(key)와 값(value)의 쌍으로 되어있는 데이터

person = {"name": "홍길동", "age": 25, "address": "서울"}

print(person)
print(person["name"], person["age"], person["address"])

person["age"] = 30
print(person)

# 키 목록
print("키 목록:", person.keys())

# 값 목록
print("값 목록:", person.values())

# 키, 값 목록
print("키, 값 목록:", person.items())

# 키 존재 확인
print('"name" 키가 존재하나요?', "name" in person)

# get()
print("이름:", person.get("name"))
print("이메일:", person.get("email", "이메일 없음"))

# 병합
extra_info = {"height": 180, "email": "test@test.com"}
person.update(extra_info)
print("병합된 딕셔너리", person)

# 중첩 딕셔너리
users = {
    "user1": {
        "name": "홍길동",
        "age": 20,
    },
    "user2": {
        "name": "김철수",
        "age": 21
    }
}
print(users)

# 복사본
person_copy = person.copy()
person_copy["name"] = '김철수'
print('원본:', person)
print('복사본:', person_copy)




