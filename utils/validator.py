def validate_order(symbol, side, order_type, quantity):
    if not symbol.endswith("USDT"):
        return False, "Symbol must end with USDT."
    if side not in ["BUY", "SELL"]:
        return False, "Side must be BUY or SELL."
    if order_type not in ["MARKET", "LIMIT","STOP_MARKET"]:
        return False, "Order type must be MARKET or LIMIT or STOP_MARKET."
    try:
        quantity = float(quantity)
        if quantity <= 0:
            return False, "Quantity must be positive."
    except ValueError:
        return False, "Quantity must be a number."
    return True, ""
def validate_inputs(symbol, side, order_type, quantity, limit_price=None):
    if not symbol or not side or not order_type or float(quantity) <= 0:
        return False
    if order_type == "LIMIT" and (limit_price is None or float(limit_price) <= 0):
        return False
    return True
def is_valid_notional(price, qty):
    return float(price) * float(qty) >= 100
