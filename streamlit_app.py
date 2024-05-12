import streamlit as st

def calculate_result(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def main():
    st.set_page_config(page_title="Calculator", page_icon=":1234:")
    st.title("Inline Calculator")

    expression = st.text_input("Enter an expression:")

    # Calculate the result in real-time as the user types
    result = calculate_result(expression)
    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()




