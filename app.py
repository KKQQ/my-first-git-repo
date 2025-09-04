import pandas as pd
import streamlit as st

st.set_page_config(page_title="My first Streamlit app te", page_icon="🧪", layout="centered")

st.title("Hello Streamlit!")
name = st.text_input("You name: ", placeholder="e.g.: Anna")
if st.button("Greet me"):
    st.success(f"Hi, {name or 'friend'}!")

st.subheader("Table")
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
st.dataframe(df)

st.subheader("Result of a calculation")
x = st.slider("Choose a number", 0, 100, 50)
st.write("Square：", x**2)