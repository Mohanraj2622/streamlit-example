import streamlit as st

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount):
        if date in self.expenses:
            self.expenses[date] += amount
        else:
            self.expenses[date] = amount

    def calculate_daily_expenses(self):
        return self.expenses

def main():
    st.title("Expense Tracker")
    tracker = ExpenseTracker()

    while True:
        choice = st.sidebar.selectbox("Menu", ["Add Expense", "View Daily Expenses", "Exit"])

        if choice == "Add Expense":
            date = st.text_input("Enter date (YYYY-MM-DD):")
            amount = st.number_input("Enter expense amount:", value=0.0)
            if st.button("Add Expense"):
                tracker.add_expense(date, amount)
                st.success("Expense added successfully!")
        elif choice == "View Daily Expenses":
            daily_expenses = tracker.calculate_daily_expenses()
            if not daily_expenses:
                st.warning("No expenses recorded yet.")
            else:
                st.subheader("Daily Expenses:")
                for date, amount in daily_expenses.items():
                    st.write(f"{date}: ${amount}")
        elif choice == "Exit":
            st.warning("Exiting...")
            break

if __name__ == "__main__":
    main()
