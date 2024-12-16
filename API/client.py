import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

    ## streamlit framework

st.title('Langchain Demo With OPEN AI API')
input_text=st.text_input("Write an essay on")

if input_text:
    st.write(get_openai_response(input_text))