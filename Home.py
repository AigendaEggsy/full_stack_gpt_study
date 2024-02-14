# https://docs.streamlit.io/library/get-started/create-an-app
import streamlit as st
from langchain.prompts import PromptTemplate


a = [1, 2, 3, 4]

d = {"x":1}

p = PromptTemplate.from_template("xxxx")

a

d

st.selectbox("Choose yout model", {"gpt3", "gpt4"})