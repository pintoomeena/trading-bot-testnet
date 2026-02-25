import logging
from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC

def place_order(client, symbol, side, order_type, quantity, price=None):
    logging.info(f"Placing order: {symbol} {side} {order_type} qty={quantity} price={price}")

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

    elif order_type == "LIMIT":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )

    logging.info(f"Order response: {order}")
    return order