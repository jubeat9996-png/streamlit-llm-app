from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

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

    if selected_item == "健康についての専門家":
        if user_input.strip():
        # LangChain用のメッセージ
            messages = [
                SystemMessage(content="あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"),
                HumanMessage(content=user_input)
            ]
            # LLM呼び出し
            response = llm(messages)
            # 結果を画面に表示
            st.write("### 回答:")
            st.write(response.content)
        else:
            st.warning("入力してください。")    
    
    elif selected_item == "投資についての専門家":
        if user_input.strip():
        # LangChain用のメッセージ
            messages = [
                SystemMessage(content="あなたは投資に関するアドバイザーです。安全なアドバイスを提供してください。"),
                HumanMessage(content=user_input)
            ]
            # LLM呼び出し
            response = llm(messages)
            # 結果を画面に表示
            st.write("### 回答:")
            st.write(response.content)
        else:
            st.warning("入力してください。")
