import streamlit as st

# st.title('My To-Do List Creator')  #ข้อความบนหัว
# my_todo_list = ["Learn Markdown", "Learn Python", "Learn Streamlit"]
# st.write('My current To-Do list is:', my_todo_list)  #เขียน
#
# new_todo = st.text_input("What do you need to do?") #ประโยค ข้อความให้ใส่
#
# if st.button('Add the new To-Do item'):  #ุให้มีปุ่ม,ชื่อในปุ่ม
#     st.write('Adding a new item to the list')  #ข้อความใต้ปุ่ม  จะขึ้นเมื่อกดปุ่ม
#     my_todo_list.append(new_todo)  #add ข้อความ text กลับไปที่ list
#
# st.write('My new To-Do list is:', my_todo_list)

# Fix
# 1. make it save to session state
#    https://docs.streamlit.io/library/api-reference/session-state
# 2. add a number input for number of day for each todo.
#    You may need to change the data structure of `my_todo_list`

st.title('My To-Do List Creator')
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = ["Learn Markdown", "Learn Python", "Learn Streamlit"]
st.write('My current To-Do list is:', st.session_state.my_todo_list)

new_todo = st.text_input("What do you need to do?")

if st.button('Add the new To-Do item'):
    st.write('Adding a new item to the list')
    st.session_state.my_todo_list.append(new_todo)

st.write('My new To-Do list is:', st.session_state.my_todo_list)


