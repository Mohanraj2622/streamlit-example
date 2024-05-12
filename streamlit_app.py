import streamlit as st

def calculate_result(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def main():
    st.set_page_config(page_title="Virtual Calculator", page_icon=":1234:")
    st.title("Virtual Calculator")

    expression = st.text_input("Enter an expression:")
    if st.button("Calculate"):
        result = calculate_result(expression)
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()



