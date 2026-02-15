import pandas as pd

def save_trades(stats, path="data/backtest_trades.csv"):
    trades = stats["_trades"]
    trades.to_csv(path, index=False)
    print(f"Backtest trades saved to {path}")
