from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

# Make sure to set OPENAI_API_KEY and LANGCHAIN_API_KEY in your environment before running this app.

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am chatbot. I am here to assist you. Please type your queries"),
        ("user", "Question:{question}")
    ]
)

st.title('LLM-OPENAI PROJECT')
input_text = st.text_input("How may I help you")

llm = ChatOpenAI(model="gpt-4.1")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))