def validate_order(symbol, side, order_type, quantity):
    if not symbol.endswith("USDT"):
        return False, "Symbol must end with USDT."
    if side not in ["BUY", "SELL"]:
        return False, "Side must be BUY or SELL."
    if order_type not in ["MARKET", "LIMIT"]:
        return False, "Order type must be MARKET or LIMIT."
    try:
        quantity = float(quantity)
        if quantity <= 0:
            return False, "Quantity must be positive."
    except ValueError:
        return False, "Quantity must be a number."
    return True, ""
