import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# --- Initial Setup ---
st.set_page_config(page_title="Business Finance Tracker", layout="wide")
st.title("📊 Business Finance Tracker")

# --- User Investment Setup ---
st.sidebar.header("User & Investment Setup")
n_users = st.sidebar.number_input("Number of Users", min_value=1, step=1)
users = {}
total_investment = 0

for i in range(n_users):
    name = st.sidebar.text_input(f"User {i+1} Name")
    investment = st.sidebar.number_input(f"{name}'s Monthly Investment ($)", min_value=0.0, step=10.0)
    users[name] = investment
    total_investment += investment

# Calculate Equity Shares
if total_investment > 0:
    shares = {user: (investment / total_investment) * 100 for user, investment in users.items()}
else:
    shares = {user: 0 for user in users}

# --- Product Management ---
st.sidebar.header("Product Management")
product_name = st.sidebar.text_input("Product Name")
buy_price = st.sidebar.number_input("Purchase Price ($)", min_value=0.0, step=0.1)
sell_price = st.sidebar.number_input("Selling Price ($)", min_value=0.0, step=0.1)

profit_margin = sell_price - buy_price
if st.sidebar.button("Add Product"):
    st.session_state.setdefault("products", []).append((product_name, buy_price, sell_price, profit_margin))

# Display Product Table
if "products" in st.session_state and st.session_state["products"]:
    st.subheader("📦 Products List")
    df_products = pd.DataFrame(st.session_state["products"], columns=["Product", "Buy Price", "Sell Price", "Profit Margin"])
    st.dataframe(df_products)

# --- Financial Overview ---
st.subheader("💰 Financial Overview")
total_revenue = sum(sell for _, _, sell, _ in st.session_state.get("products", []))
total_profit = sum(profit for _, _, _, profit in st.session_state.get("products", []))

st.metric("Total Revenue", f"${total_revenue:.2f}")
st.metric("Total Profit", f"${total_profit:.2f}")

# Profit Distribution
profit_distribution = {user: (share / 100) * total_profit for user, share in shares.items()}

# --- Visualization ---
st.subheader("📉 Profit Distribution")
fig, ax = plt.subplots()
ax.bar(profit_distribution.keys(), profit_distribution.values(), color='green')
ax.set_ylabel("Profit ($)")
ax.set_title("Profit Share per User")
st.pyplot(fig)

# --- Export Options ---
def export_csv():
    df = pd.DataFrame(list(profit_distribution.items()), columns=["User", "Profit Share ($)"])
    df.to_csv("profit_distribution.csv", index=False)
    st.success("CSV Exported Successfully!")

def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Profit Distribution Report", ln=True, align='C')
    pdf.ln(10)
    for user, profit in profit_distribution.items():
        pdf.cell(200, 10, f"{user}: ${profit:.2f}", ln=True)
    pdf.output("profit_distribution.pdf")
    st.success("PDF Exported Successfully!")

st.sidebar.subheader("Export Data")
if st.sidebar.button("Export CSV"):
    export_csv()
if st.sidebar.button("Export PDF"):
    export_pdf()

