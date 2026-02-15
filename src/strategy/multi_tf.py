import pandas as pd
from ta.trend import SMAIndicator
from src.strategy.base import BaseStrategy

class MultiTFStrategy(BaseStrategy):
    """
    SINGLE SOURCE OF TRUTH
    Used identically in backtesting and live trading
    """

    def __init__(self, fast=9, slow=21):
        self.fast = fast
        self.slow = slow

    def generate_signal(self, df_15m: pd.DataFrame, df_1h: pd.DataFrame):
        if len(df_15m) < self.slow + 2 or len(df_1h) < self.slow:
            return None

        # 1H trend confirmation
        sma_1h = SMAIndicator(df_1h["close"], self.slow).sma_indicator()
        trend = "BULL" if df_1h["close"].iloc[-1] > sma_1h.iloc[-1] else "BEAR"

        # 15M crossover
        sma_fast = SMAIndicator(df_15m["close"], self.fast).sma_indicator()
        sma_slow = SMAIndicator(df_15m["close"], self.slow).sma_indicator()

        pf, cf = sma_fast.iloc[-2], sma_fast.iloc[-1]
        ps, cs = sma_slow.iloc[-2], sma_slow.iloc[-1]

        if trend == "BULL" and pf <= ps and cf > cs:
            return {"signal": "BUY", "price": df_15m["close"].iloc[-1]}

        if trend == "BEAR" and pf >= ps and cf < cs:
            return {"signal": "SELL", "price": df_15m["close"].iloc[-1]}

        return None
