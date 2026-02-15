# Backtesting engine entry point

import pandas as pd
from backtesting import Backtest
from src.backtesting.backtest import BacktestEngine
from src.backtesting.analyzer import save_trades

# Load REAL historical data
df_15m = pd.read_csv("data/BTCUSDT_15m.csv", index_col=0, parse_dates=True)
df_1h = pd.read_csv("data/BTCUSDT_1h.csv", index_col=0, parse_dates=True)

# Attach higher timeframe data
df_15m.df_1h = df_1h

bt = Backtest(
    df_15m,
    BacktestEngine,
    cash=10000,
    commission=0.001
)

stats = bt.run()
save_trades(stats)   # → data/backtest_trades.csv
