import streamlit as st
from bot import place_order
from utils.validator import validate_order

st.title("🪙 PrimeTrade Bot (Binance Futures Testnet)🪙")
st.markdown("Place live **testnet orders** on Binance Futures securely.By Tanmay")

symbol = st.text_input("Symbol", value="BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.01, value=0.01)

if st.button("Place Order"):
    valid, message = validate_order(symbol, side, order_type, quantity)
    if not valid:
        st.error(f"❌ {message}")
    else:
        with st.spinner("Placing order..."):
            result, error = place_order(symbol, side, order_type, quantity)
            if error:
                st.error(f"❌ Error: {error}")
            else:
                st.success("✅ Order placed successfully.")
                st.json(result)
