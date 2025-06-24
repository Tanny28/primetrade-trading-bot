from binance.um_futures import UMFutures
from utils.logger import log_order
from utils.validator import validate_inputs
from config import API_KEY, API_SECRET

def place_order(symbol, side, order_type, quantity, limit_price=None):
    client = UMFutures(key=API_KEY, secret=API_SECRET, base_url="https://testnet.binancefuture.com")
    
    if not validate_inputs(symbol, side, order_type, quantity, limit_price):
        return {"error": "Invalid input parameters."}

    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }
        if order_type == "LIMIT":
            if not limit_price:
                return {"error": "Limit price is required for LIMIT orders."}
            params.update({
                "price": str(limit_price),
                "timeInForce": "GTC"
            })

        order = client.new_order(**params)
        log_order(order)
        return order

    except Exception as e:
        log_order(f"Error: {str(e)}")
        return {"error": str(e)}
