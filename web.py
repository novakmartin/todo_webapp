import streamlit as st
import functions as fns


def add_todo():
    new_todo = st.session_state['user_input']+'\n'
    todos = fns.get_todos()
    todos.append(new_todo)
    fns.write_todos(todos)


st.title('Slovenia trip inventory')
st.subheader('What do we need on the trip?')

todos = fns.get_todos()

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        fns.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label='Add a Todo',
              placeholder="Add a Todo..",
              label_visibility='hidden',
              on_change=add_todo,
              key='user_input')
