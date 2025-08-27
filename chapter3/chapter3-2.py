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

st.markdown("---") # 구분선

st.subheader("📋 현재 할 일 목록")

# 삭제할 할 일들의 인덱스를 저장할 리스트
remove_indices = []

# enumerate를 사용하여 할 일의 인덱스와 내용을 함께 가져옴
if st.session_state['tasks']:
    for i, task in enumerate(st.session_state['tasks']):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15]) # 할 일, 체크박스, 삭제 버튼 공간 분할

        with col1:
            # 체크박스를 먼저 표시하고, 그 옆에 텍스트를 표시
            checked = st.checkbox(f"{task['text']}", value=task['done'], key=f"check_task_{i}")
            if checked != st.session_state['tasks'][i]['done']: # 상태 변경 감지
                st.session_state['tasks'][i]['done'] = checked
                save_tasks(st.session_state['tasks']) # 변경 사항 저장
                st.experimental_rerun() # 앱을 다시 실행하여 변경 사항 반영

        with col2:
            if st.button("삭제", key=f"delete_task_{i}"):
                remove_indices.append(i) # 삭제할 할 일의 인덱스 추가

    # 할 일 삭제는 반복문이 끝난 후에 처리 (인덱스 오류 방지)
    # 큰 인덱스부터 삭제해야 리스트의 순서가 섞이지 않음
    for idx in sorted(remove_indices, reverse=True):
        del st.session_state['tasks'][idx]
        st.info(f"할 일이 삭제되었습니다.")
    if remove_indices: # 삭제가 발생했으면 데이터 저장 및 앱 새로고침
        save_tasks(st.session_state['tasks'])
        st.experimental_rerun() # 변경 사항 반영

    # 모든 할 일을 완료했을 때 축하 메시지
    done_tasks_count = sum(1 for task in st.session_state['tasks'] if task['done'])
    total_tasks_count = len(st.session_state['tasks'])

    st.markdown(f"---")
    st.info(f"완료된 할 일: {done_tasks_count} / {total_tasks_count}")

    if total_tasks_count > 0 and done_tasks_count == total_tasks_count:
        st.balloons() # 풍선 효과!
        st.success("🎉 모든 할 일을 완료했습니다! 축하합니다!")
else:
    st.info("아직 할 일이 없습니다. 새로운 할 일을 추가해보세요!")