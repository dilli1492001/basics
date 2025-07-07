import streamlit as st
import requests

st.title("Rhyming Words Finder*****")
word = st.text_input("enter your word ",placeholder="Eg- donkey")
is_clicked = st.button("generator",type = "primary")
if is_clicked:
    endpoint = f"https://api.datamuse.com/words?sp={word}"
    response = requests.get(endpoint)
    data = response.json()
    if response.status_code == 200:
        for item in data:
            st.write(item.get("word"))
    else :
        st.toast("somethingwent wrong")