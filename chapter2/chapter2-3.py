import streamlit as st

st.header("Streamlit 핵심 부품들 심화")

# 텍스트 입력창 (st.text_input)
user_name_comp = st.text_input("이름을 입력하세요:", key="user_name_comp")
if user_name_comp:
    st.write(f"환영합니다, {user_name_comp}님!")

# 버튼 (st.button)
if st.button("인사하기", key="greet_button_comp"):
    st.write("반갑습니다!")

# 체크박스 (st.checkbox)
if st.checkbox("이용 약관에 동의합니다", key="agree_checkbox_comp"):
    st.success("동의하셨군요! 서비스를 이용할 수 있습니다.")
else:
    st.warning("동의하지 않았습니다. 서비스를 이용할 수 없습니다.")

# 슬라이더 (st.slider): 숫자 범위 선택
age = st.slider("나이를 선택하세요:", 0, 100, 25, key="age_slider_comp") # (최소, 최대, 기본값)
st.write(f"선택한 나이: {age}세")

# 셀렉트 박스 (st.selectbox): 드롭다운 메뉴에서 옵션 선택
option = st.selectbox(
    "가장 좋아하는 색깔은?",
    ("빨강", "파랑", "초록", "노랑"),
    key="color_selectbox_comp"
)
st.write(f"선택한 색깔: {option}")

st.markdown("---")
st.subheader("`st.session_state`의 마법")

# session_state에 'click_count'라는 키가 없으면 0으로 초기화
if 'click_count' not in st.session_state:
    st.session_state['click_count'] = 0

st.write(f"버튼이 눌린 횟수: {st.session_state['click_count']}")

# 버튼을 누르면 'click_count' 값을 1 증가시키고 세션 상태에 저장
if st.button("카운트 증가시키기", key="increment_button"):
    st.session_state['click_count'] += 1
    st.write(f"카운트 증가! 현재 횟수: {st.session_state['click_count']}")

# Streamlit 앱 다시 실행 (rerun) 안내
st.info("코드를 수정하고 저장하면 앱이 자동으로 업데이트됩니다. 놀랍죠?")
st.warning("`st.experimental_rerun()`은 특정 조건에서만 앱을 강제로 새로고침 할 때 사용합니다. 일반적으로는 Streamlit이 자동으로 변경 사항을 감지하여 리로드됩니다.")