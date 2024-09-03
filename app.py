import streamlit as st 

st.title("All About Brigette Icong")

text = st.text_area('Basic Information:')

if st.button("Show text"):
    st.write(text) 