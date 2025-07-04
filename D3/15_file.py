# 파일 입출력

# # 파일열기
# file = open("테스트.txt", "w", encoding="utf-8")

# # 파일에 내용 쓰기
# file.write("안녕하세요 반갑습니다")

# # 파일 닫기
# file.close()
# print("파일에 텍스트 입력 완료")

# # 파일 읽기
# file = open("테스트.txt", "r", encoding="utf-8")
# content = file.read()
# file.close()

# print(content)


# # with open
# lines = ["첫 번째 줄\n", "두 번째 줄\n", "세 번째 줄\n"]

# # 파일 생성, 덮어쓰기 w
# with open("multiline.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# # 파일 읽어오기 r
# with open("multiline.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(f"읽은 줄: ", line.strip())

# 수정 a
# with open("테스트.txt", "a", encoding="utf-8") as file:
#     file.write("\n추가된 내용입니다")
