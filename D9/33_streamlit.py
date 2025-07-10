import streamlit as st

# 사이트 제목
st.title("웹사이트 제목")

# 텍스트 출력
st.write("안녀앟세요")

age = st.number_input("나이를 입력하세요: ", min_value=1, max_value=100)
name = st.text_input("이름을 입력하세요: ")

# 버튼
if st.button("인사하기"):
    st.success(f"안녕하세요 {name}이고, {age}살입니다")

# 체크박스
if st.checkbox("추가 정보 보기"):
    st.info("체크박스를 잘 눌렀습니다")
