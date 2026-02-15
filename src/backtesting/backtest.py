from backtesting import Strategy
from src.strategy.multi_tf import MultiTFStrategy

class BacktestEngine(Strategy):
    fast = 9
    slow = 21

    def init(self):
        self.logic = MultiTFStrategy(self.fast, self.slow)
        self.df_1h = self.data.df_1h

    def next(self):
        current_time = self.data.df.index[-1]
        df_1h_slice = self.df_1h[self.df_1h.index <= current_time]

        signal = self.logic.generate_signal(self.data.df, df_1h_slice)
        if not signal:
            return

        if signal["signal"] == "BUY":
            self.buy()
        elif signal["signal"] == "SELL":
            self.sell()
