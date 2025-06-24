from binance.enums import *
from config import get_binance_client
from utils.logger import log_info, log_error

client = get_binance_client()

def place_order(symbol, side, order_type, quantity):
    try:
        params = {
            "symbol": symbol,
            "side": SIDE_BUY if side == "BUY" else SIDE_SELL,
            "type": ORDER_TYPE_MARKET if order_type == "MARKET" else ORDER_TYPE_LIMIT,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params.update({
                "timeInForce": TIME_IN_FORCE_GTC,
                "price": "20000"  # Dummy limit price, update as needed
            })

        order = client.futures_create_order(**params)
        log_info(f"Order placed: {order}")
        return order, None
    except Exception as e:
        log_error(str(e))
        return None, str(e)
