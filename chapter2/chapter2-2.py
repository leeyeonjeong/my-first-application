import streamlit as st

st.header("Chapter 2-2 함수 예제")

# 1. 인사말을 출력하는 함수 (인자 있음, 반환값 없음)
def greet(name):
    st.write(f"안녕하세요, {name}님!")

greet("김코딩")

# 2. 숫자를 두 배로 만들고 반환하는 함수 (인자 있음, 반환값 있음)
def double_number(num):
    result = num * 2
    return result

# 3. Streamlit 앱 내에서 함수 호출
user_name_for_greet = st.text_input("이름을 입력하시면 인사해 드려요:", key="greet_input")
if user_name_for_greet:
    greet(user_name_for_greet) # 함수 호출

my_num = st.number_input("숫자를 입력하세요:", value=5, key="double_input")
if st.button("두 배로 만들기", key="double_button"):
    doubled_result = double_number(my_num) # 함수 호출 및 반환값 사용
    st.write(f"{my_num}의 두 배는 {doubled_result}입니다.")

st.markdown("---")

# 4. 함수를 활용하여 Streamlit 컴포넌트 만들기 예시 (코드 재사용)
st.subheader("함수로 버튼 만들기")
def create_custom_button(label, key_name, message):
    if st.button(label, key=key_name):
        st.info(f"'{label}' 버튼이 눌렸습니다! {message}")

create_custom_button("첫 번째 버튼", "first_custom_button", "이것은 첫 번째 메시지입니다.")
create_custom_button("두 번째 버튼", "second_custom_button", "이것은 두 번째 메시지입니다.")
create_custom_button("세 번째 버튼", "third_custom_button", "간단하게 재사용하죠?")