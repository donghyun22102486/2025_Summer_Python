# import requests

# # 이름에 따라 예상 나이를 추측해주는 무료 API
# url = "https://api.agify.io?name=alice"
# response = requests.get(url)

# print("응답 코드:", response.status_code)
# print("응답 데이터:", response.json())


# import requests

# url = "https://httpbin.org/post"
# data = {"username": "admin", "password": "1234"}

# response = requests.post(url, data=data)

# # print(response.json())
# # response.json() >> 이거 딕셔너리임
# # ["form"] 해주면 form에 들어있는 값만 나옴
# print("응답 코드:", response.status_code)
# print("요청 본문 내용:", response.json()["form"])


import requests

names = ["minho", "jenny", "david", "yuna"]

for name in names:
    url = f"https://api.agify.io?name={name}"
    response = requests.get(url)
    data = response.json()
    print(f"{data['name']}의 예상 나이: {data['age']}")
