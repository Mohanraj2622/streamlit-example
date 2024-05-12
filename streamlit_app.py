import streamlit as st

def main():
    st.set_page_config(page_title="Virtual Calculator", page_icon=":1234:")
    st.title("Virtual Calculator")

    # Initialize the expression variable
    expression = ""

    # Display the expression input field
    expression = st.text_input("Enter an expression:", value=expression, key="expression")

    # Create a placeholder for the result
    result = None

    # Create buttons for each digit and operator
    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        if st.button("7"):
            expression += "7"
    with col2:
        if st.button("8"):
            expression += "8"
    with col3:
        if st.button("9"):
            expression += "9"
    with col4:
        if st.button("/"):
            expression += "/"

    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        if st.button("4"):
            expression += "4"
    with col2:
        if st.button("5"):
            expression += "5"
    with col3:
        if st.button("6"):
            expression += "6"
    with col4:
        if st.button("*"):
            expression += "*"

    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        if st.button("1"):
            expression += "1"
    with col2:
        if st.button("2"):
            expression += "2"
    with col3:
        if st.button("3"):
            expression += "3"
    with col4:
        if st.button("-"):
            expression += "-"

    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        if st.button("0"):
            expression += "0"
    with col2:
        if st.button("."):
            expression += "."
    with col3:
        if st.button("DEL"):
            expression = expression[:-1]
    with col4:
        if st.button("+"):
            expression += "+"

    # Add a button to calculate the result
    if st.button("Calculate"):
        try:
            result = eval(expression)
        except Exception as e:
            result = "Error"
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()



