import streamlit as st
import datetime


def calculate_bmi(height, weight):
    height = height / 100
    bmi = weight / (height**2)
    return round(bmi, 2)


st.title("BMI 계산하기")

st.header("사용자 정보 입력")

name = st.text_input("이름: ")
birth = st.date_input("생년월일: ", value=datetime.date(2000, 1, 1))

st.markdown("---")

height = st.slider("키 (cm)", 100, 220, step=1)
weight = st.slider("몸무게 (kg)", 30, 200, step=1)

# 버튼으로 실행
if st.button("BMI 계산하기"):
    bmi_result = calculate_bmi(height, weight)
    st.success(f"{name}님의 BMI는 {bmi_result}입니다")

    if bmi_result < 18.5:
        st.warning("저체중입니다")
    elif bmi_result < 23:
        st.info("정상입니다")
    elif bmi_result < 25:
        st.warning("과체중입니다")
    else:
        st.error("비만입니다.")


# 사진 업로드
photo = st.file_uploader("사진을 업로드하세요", type=["jpg", "png"])
if photo:
    st.image(photo, caption="사진입니다")
