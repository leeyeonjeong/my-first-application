import streamlit as st
import json
import os

# 데이터 파일 경로 설정
TASKS_FILE = 'data/tasks.json'

# 파일에서 할 일 데이터를 로드하는 함수
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 할 일 데이터를 파일에 저장하는 함수
def save_tasks(tasks):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True) # data 폴더가 없으면 생성
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task():
    new_task = st.session_state.get("new_task_input", "").strip()
    if new_task:
        st.session_state['tasks'].append({"text": new_task, "done": False}) # 할 일 내용과 완료 여부 저장
        save_tasks(st.session_state['tasks']) # 데이터 저장
        st.success(f"'{new_task}'가 추가되었습니다!")
        st.session_state["new_task_input"] = ""

# 앱 시작 시 할 일 데이터 로드 및 session_state 초기화
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

# 앱 전역 설정
st.set_page_config(
    page_title="나만의 할 일 리스트",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("📝 나만의 할 일 리스트")

# 할 일 입력 창
st.text_input("새로운 할 일을 입력하세요:", key="new_task_input")

st.button("할 일 추가", on_click=add_task)