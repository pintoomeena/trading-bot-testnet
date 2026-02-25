import argparse
import logging

from bot.client import get_binance_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validate CLI inputs
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Get Binance client
        client = get_binance_client()

        print("\nOrder Request:")
        print(vars(args))

        # Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Print full raw response
        print("\nOrder Response (Raw):")
        print(order)

        # Parsed, safe summary
        print("\nParsed Summary:")
        print("Order ID:", order.get("orderId", order.get("order_id")))
        print("Status:", order.get("status"))
        print("Original Qty:", order.get("origQty"))
        print(
            "Executed Qty:",
            order.get("executedQty", order.get("cumQty"))
        )
        print(
            "Average Price:",
            order.get("avgPrice", "Will be available after fill")
        )

        print("\nSUCCESS ✅")

    except Exception as e:
        logging.error(e)
        print("\nFAILED ❌:", e)


if __name__ == "__main__":
    main()