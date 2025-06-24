import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def get_binance_client():
    return Client(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET"),
        testnet=True
    )
