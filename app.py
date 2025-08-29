from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)


def get_llm_response(user_input: str, selected_item: str):
    
    if selected_item == "健康についての専門家":
        messages = [
            SystemMessage(content="あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"),
            HumanMessage(content=user_input)
        ]
    elif selected_item == "投資についての専門家":
        messages = [
            SystemMessage(content="あなたは投資に関するアドバイザーです。安全なアドバイスを提供してください。"),
            HumanMessage(content=user_input)
        ]
    
    response = llm(messages)
    return response.content



st.title("LLM相談アプリ")

selected_item = st.radio(
    "相談する専門家を選択してください。",
    ["健康についての専門家", "投資についての専門家"]
)

st.divider()

# 入力フォーム
user_input = st.text_input("質問を入力してください:")

if st.button("実行"):
    st.divider()

    if user_input.strip():
        response = get_llm_response(user_input, selected_item)
        st.write("### 回答:")
        st.write(response)
    else:
        st.warning("入力してください。")    
