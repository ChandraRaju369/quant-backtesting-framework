import time
import csv
from src.trading.exchange import BinanceClient
from config.config import SYMBOL, ORDER_QTY

class LiveTrader:
    def __init__(self, strategy):
        self.strategy = strategy
        self.client = BinanceClient(testnet=True)
        self.last_candle = None
        self.position = None

    def run(self):
        while True:
            df_15m = self.client.get_ohlcv(SYMBOL, "15m")
            df_1h = self.client.get_ohlcv(SYMBOL, "1h")

            candle_time = df_15m.index[-1]
            if candle_time == self.last_candle:
                time.sleep(10)
                continue

            self.last_candle = candle_time
            signal = self.strategy.generate_signal(df_15m, df_1h)

            if signal and self.position is None:
                order = self.client.place_market_order(
                    SYMBOL, signal["signal"], ORDER_QTY
                )
                fill_price = float(order["fills"][0]["price"])
                self.position = signal["signal"]

                with open("data/live_trades.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        order["transactTime"],
                        SYMBOL,
                        signal["signal"],
                        signal["price"],
                        fill_price
                    ])

            time.sleep(60)
