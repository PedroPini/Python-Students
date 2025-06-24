import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Initialize session State
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Type", "Category", "Amount"])

#Initialize our CSV file
CSV_FILE = "finance_data.csv"
HEADERS = ["Date", "Type", "Category", "Amount"]

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=HEADERS).to_csv(CSV_FILE, index=False)

#Calculate Balance
def calculate_balance(df):
    income_total = df[df["Type"] == "Income"]["Amount"].sum()
    expense_total = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = income_total - expense_total
    return income_total, expense_total, balance

#Load existing data
def load_data():
    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["Date"])
        # Update session state
        st.session_state.data = df
        return df
    except:
        return pd.DataFrame(columns=HEADERS)
    
# Input form function
def input_form():
    with st.form("entry_form", clear_on_submit=True):
        #create visual grids so each input is not displayed row by row
        col1, col2, col3 = st.columns(3) # Date | Type | Category

        with col1:
            date = st.date_input("Date", datetime.today())
        with col2:
            type_ = st.selectbox("Type", ["Expense", "Income"])
        with col3:
            category = st.selectbox(
                "Expense or Income",
                ["Rent", "Salary", "Mobile Phone", "Internet", "Groceries", "Utilities", "Others"],
                placeholder="Select a category..."
            )

        amount = st.number_input("Amount. ($)", min_value=0.0, format="%.2f", key="amount_input")

        submitted = st.form_submit_button("Save Entry")

        if submitted:
            #validate form values
            if not category:
                st.error("Please enter a category")
                return
            if amount <=0:
                st.error("Amount must be greather than 0")
                return
            
            new_entry = pd.DataFrame({
                "Date": [date],
                "Type": [type_],
                "Category": [category],
                "Amount": [amount]
            })

            #append to CSV
            new_entry.to_csv(CSV_FILE, mode='a', header=False, index=False)

            # Reload Data
            load_data()
            st.success("Entry saved!")
            st.rerun()

def display_charts(df):
    #Filter expenses for pie chart
    expenses = df[df["Type"] == "Expense"]

    if not expenses.empty:
        # Pie chart
        col1, col2 = st.columns(2)

        #Pie Chart
        with col1:
            st.subheader("Spending Category")
            fig1, ax1 = plt.subplots()
            category_totals = expenses.groupby("Category")["Amount"].sum()
            category_totals.plot.pie(autopct="%1.1f%%", ax=ax1)
            ax1.set_ylabel("")
            st.pyplot(fig1)

        #Monthly Trend
        with col2:
            st.subheader("Monthly Spending Trend")
            expenses['Month'] = expenses['Date'].dt.to_period('M').astype(str)
            monthly_expenses = expenses.groupby('Month')['Amount'].sum()

        