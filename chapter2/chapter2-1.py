import streamlit as st

st.header("Chapter 2-1 파이썬 기초")

# 1. 변수: 정보 담기
name = "김코딩"
age = 30
st.write(f"변수 예시: 이름: {name}, 나이: {age}") # f-string으로 쉽게 출력

# 2. 리스트: 여러 정보 나열 (순서가 있는 데이터 묶음)
fruits = ["사과", "바나나", "오렌지"]
st.write(f"리스트 예시: 좋아하는 과일: {fruits}")
st.write(f"첫 번째 과일: {fruits[0]}") # 리스트의 첫 번째 요소 접근

# 3. 딕셔너리: 이름-값 쌍으로 정보 저장 (키와 값으로 이루어진 데이터)
person_info = {"이름": "박개발", "직업": "개발자", "나이": 28}
st.write(f"딕셔너리 예시: 개인 정보: {person_info}")
st.write(f"박개발님의 직업: {person_info['직업']}") # 딕셔너리의 값 접근

# 4. 조건문: 만약 ~라면 (특정 조건에 따라 다른 동작)
score = st.slider("점수를 입력하세요:", 0, 100, 75, key="score_slider")
if score >= 60:
    st.success(f"점수 {score}점으로 합격입니다!")
else:
    st.error(f"점수 {score}점으로 불합격입니다.")

# 5. 반복문: 여러 번 반복하기 (특정 작업을 반복 수행)
st.subheader("반복문 예시")
st.write("좋아하는 과일 목록:")
for fruit in fruits: # 리스트의 각 요소를 하나씩 꺼내 반복
    st.write(f"- {fruit}")

st.write("카운트다운:")
count = 0
while count < 3: # 조건이 True인 동안 반복
    st.write(f"반복 {count}회")
    count += 1 # 카운트 증가