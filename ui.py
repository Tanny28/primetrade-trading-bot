import streamlit as st
from bot import place_order
from utils.validator import validate_order
from utils.validator import is_valid_notional


st.set_page_config(page_title="PrimeTrade Bot", layout="centered")
st.title("🪙 PrimeTrade Bot (Binance Futures Testnet)🪙")
st.markdown("Place live **testnet orders** on Binance Futures securely.By Tanmay")

symbol = st.selectbox("Symbol", ["BTCUSDT", "ETHUSDT"])
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_MARKET"])
qty = st.number_input("Quantity", min_value=0.01, step=0.01)
 
 
price = None
if order_type in ["LIMIT", "STOP_MARKET"]:
    price = st.number_input("Price", min_value=0.01, step=0.01)

if st.button("Place Order"):
    if order_type in ["LIMIT", "STOP_MARKET"] and not price:
        st.error("Please enter a valid price for this order type.")
    elif not is_valid_notional(price if price else 50000, qty):  # assuming price ~ 50,000 for MARKET
        st.error("❌ Trade value must be at least $100. Please increase the quantity or use another symbol.")
    else:
        try:
            response = place_order(symbol, side, order_type, qty, price)
            st.success("✅ Order placed successfully!")
            st.json(response)
        except Exception as e:
            st.error(f"❌ Error placing order: {str(e)}")