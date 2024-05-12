import streamlit as st
from streamlit_ace import st_ace

def calculate_result(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def main():
    st.set_page_config(page_title="Real-time Calculator", page_icon=":1234:")
    st.title("Real-time Calculator")

    expression = st_ace(
        value="",
        placeholder="Enter an expression...",
        language="text",
        height=100,
        font_size=18,
        theme="chrome",
    )

    result = calculate_result(expression)
    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()





