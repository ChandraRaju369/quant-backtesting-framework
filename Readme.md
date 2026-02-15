# Multi-Timeframe Trading Strategy

## Strategy
- 15-minute SMA(9/21) crossover
- 1-hour SMA(21) trend confirmation
- Deterministic, candle-close based

## Architecture
- Single strategy class reused for backtest & live
- Clear separation of data, logic, execution

## Data Source

Historical OHLCV data (15m and 1h) was collected directly from the
Binance REST API and stored locally as CSV files.

Backtest trades were generated using backtesting.py.
Live trades were executed on Binance Testnet using the same strategy logic.

## Backtesting
- Implemented with backtesting.py
- Trades logged to backtest_trades.csv
- No lookahead bias

## Live Trading
- Binance Testnet execution
- Same strategy logic as backtesting
- Trades logged to live_trades.csv

## Validation
- Backtest vs live trades matched by
  direction, timing, and price
- Differences only due to latency/slippage

