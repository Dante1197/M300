import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("📊 Business Finance Tracker")

# Sidebar: User Investment Input
st.sidebar.header("💰 Investment Setup")
num_users = st.sidebar.number_input("Number of Participants", min_value=1, step=1, value=1)
user_contributions = {}
total_investment = 0

for i in range(num_users):
    name = st.sidebar.text_input(f"Participant {i+1} Name", f"User {i+1}")
    contribution = st.sidebar.number_input(f"{name}'s Monthly Investment ($)", min_value=0.0, value=500.0)
    user_contributions[name] = contribution
    total_investment += contribution

# Calculate profit shares
investment_shares = {user: (contrib / total_investment) for user, contrib in user_contributions.items()}

# Sidebar: Product Management
st.sidebar.header("📦 Product Management")
if "products" not in st.session_state:
    st.session_state["products"] = []

product_name = st.sidebar.text_input("Product Name")
buy_price = st.sidebar.number_input("Purchase Price ($)", min_value=0.0, format="%.2f")
sell_price = st.sidebar.number_input("Selling Price ($)", min_value=0.0, format="%.2f")
sales = st.sidebar.number_input("Units Sold", min_value=0, step=1)

if st.sidebar.button("➕ Add Product"):
    if product_name and buy_price and sell_price:
        st.session_state["products"].append({
            "name": product_name,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "sales": sales
        })
        st.success(f"Added {product_name} to product list!")

# Product List with Edit/Delete Options
st.subheader("📦 Product List")
for i, product in enumerate(st.session_state["products"]):
    col1, col2, col3 = st.columns([3, 1, 1])
    col1.text(f"{product['name']} - Bought: ${product['buy_price']}, Sold: ${product['sell_price']}, Sales: {product['sales']}")
    if col2.button(f"✏️ Edit {i}"):
        st.session_state["products"][i]["buy_price"] = st.number_input(f"Edit Buy Price for {product['name']}", value=product['buy_price'])
        st.session_state["products"][i]["sell_price"] = st.number_input(f"Edit Sell Price for {product['name']}", value=product['sell_price'])
    if col3.button(f"❌ Delete {i}"):
        st.session_state["products"].pop(i)
        st.experimental_rerun()

# Sidebar: Bundle Feature
st.sidebar.header("📦 Create Product Bundles")
bundle_name = st.sidebar.text_input("Bundle Name")
bundle_items = st.sidebar.multiselect("Select Products for Bundle", [p["name"] for p in st.session_state["products"]])
if st.sidebar.button("➕ Create Bundle"):
    if bundle_name and bundle_items:
        st.session_state["products"].append({"name": bundle_name, "buy_price": sum([p["buy_price"] for p in st.session_state["products"] if p["name"] in bundle_items]), "sell_price": sum([p["sell_price"] for p in st.session_state["products"] if p["name"] in bundle_items]), "sales": 0})
        st.success(f"Bundle {bundle_name} created!")

# Monthly Business Expenses
st.sidebar.header("💸 Monthly Business Expenses")
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

expense_name = st.sidebar.text_input("Expense Name")
expense_amount = st.sidebar.number_input("Amount ($)", min_value=0.0, format="%.2f")
expense_type = st.sidebar.selectbox("Type", ["Monthly", "Yearly"])

if st.sidebar.button("➕ Add Expense"):
    if expense_name and expense_amount:
        st.session_state["expenses"].append({"name": expense_name, "amount": expense_amount, "type": expense_type})
        st.success(f"Added {expense_name} expense!")

# Expense List
st.subheader("💸 Expense List")
monthly_expenses = sum([e["amount"] for e in st.session_state["expenses"] if e["type"] == "Monthly"])
yearly_expenses = sum([e["amount"] for e in st.session_state["expenses"] if e["type"] == "Yearly"])
st.write(f"**Total Monthly Expenses:** ${monthly_expenses}")
st.write(f"**Total Yearly Expenses:** ${yearly_expenses}")

# Profit Calculation
profit = sum([(p["sell_price"] - p["buy_price"]) * p["sales"] for p in st.session_state["products"]]) - monthly_expenses

# Profit Sharing Calculation
st.subheader("💰 Profit Sharing")
for user, share in investment_shares.items():
    st.write(f"{user}: ${profit * share:.2f} ({share*100:.2f}% share)")

# Currency Converter
st.sidebar.header("💱 Currency Converter")
currency_options = {"USD": 1.0, "EUR": 0.92, "GBP": 0.76, "CHF": 0.98}
amount = st.sidebar.number_input("Amount in USD", min_value=0.0, format="%.2f")
target_currency = st.sidebar.selectbox("Convert to", list(currency_options.keys()))
converted_amount = amount * currency_options[target_currency]
st.sidebar.write(f"Converted: {converted_amount:.2f} {target_currency}")

# Export Options
if st.button("📤 Export Data"):
    df = pd.DataFrame(st.session_state["products"])
    df.to_csv("business_data.csv", index=False)
    st.success("✅ Data exported!")
