import pandas as pd
import streamlit as st

st.set_page_config(page_title="我的第一个 Streamlit 应用", page_icon="🧪", layout="centered")

st.title("Hello Streamlit 👋")
name = st.text_input("你的名字：", placeholder="比如：Anna")
if st.button("打招呼"):
    st.success(f"Hi, {name or '朋友'}!")

st.subheader("小表格")
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
st.dataframe(df)

st.subheader("滑块 + 动态结果")
x = st.slider("选择一个数字", 0, 100, 50)
st.write("平方：", x**2)