import streamlit as st
import requests

st.title("AI-Powered Knowledge Assistant")

st.write("Ask any question and get AI-generated answers.")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        response = requests.post("http://localhost:5000/chat", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("answer", "No response received.")
            st.write(f"**Answer:** {answer}")
        else:
            st.error("Error fetching response from backend.")
    else:
        st.warning("Please enter a question.")
