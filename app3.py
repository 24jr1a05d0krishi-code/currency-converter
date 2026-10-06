import streamlit as st

st.set_page_config(
    page_title="Krishi Sowja Currency Converter",
    page_icon="💱"
)

st.title("💱 Krishi Sowja Currency Converter")

st.write("Convert currency easily using this application.")

rates = {
    "INR": 1.00,
    "USD": 83.50,
    "EUR": 90.50,
    "GBP": 105.00
}

amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=100.0
)

from_currency = st.selectbox(
    "From Currency",
    ["INR", "USD", "EUR", "GBP"]
)

to_currency = st.selectbox(
    "To Currency",
    ["INR", "USD", "EUR", "GBP"]
)

if st.button("💱 Convert"):

    amount_in_inr = amount * rates[from_currency]

    converted_amount = amount_in_inr / rates[to_currency]

    st.success(
        f"{amount:.2f} {from_currency} = "
        f"{converted_amount:.2f} {to_currency}"
    )