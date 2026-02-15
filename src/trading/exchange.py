from binance.client import Client
import pandas as pd
from config.config import BINANCE_API_KEY, BINANCE_API_SECRET

class BinanceClient:
    def __init__(self, testnet=True):
        self.client = Client(
            BINANCE_API_KEY,
            BINANCE_API_SECRET,
            testnet=testnet
        )

    def get_ohlcv(self, symbol, interval, limit=50):
        klines = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        df = pd.DataFrame(klines, columns=[
            "time","open","high","low","close","volume",
            "c1","c2","c3","c4","c5","c6"
        ])
        df["time"] = pd.to_datetime(df["time"], unit="ms")
        df.set_index("time", inplace=True)
        return df[["open","high","low","close","volume"]].astype(float)

    def place_market_order(self, symbol, side, qty):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )
