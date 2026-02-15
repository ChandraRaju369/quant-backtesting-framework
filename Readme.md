# Multi-Timeframe Trading Strategy Framework

## Overview
This project implements a deterministic multi-timeframe quantitative trading strategy with strict parity between backtesting and live execution. The system is designed to reuse the same core strategy logic across both environments to ensure reproducibility, consistency, and no lookahead bias.

## Strategy
- 15-minute SMA (9/21) crossover for entry signals
- 1-hour SMA (21) for higher timeframe trend confirmation
- Fully deterministic and candle-close based execution
- No lookahead bias in signal generation

## Key Features
- Deterministic trading logic
- Backtest and live execution parity
- Modular architecture (data, strategy, execution)
- Trade logging and validation
- Reproducible results using stored datasets

## Architecture
- Single strategy class reused for both backtesting and live trading
- Clear separation of:
  - Data Layer (OHLCV ingestion)
  - Strategy Logic Layer
  - Execution Engine
  - Validation & Logging Layer

Detailed system design is documented in `ARCHITECTURE.md`.

## Data Source
Historical OHLCV data (15m and 1h) was collected using the Binance REST API and stored locally as CSV files for reproducible experiments and deterministic backtesting.

## Backtesting
- Implemented using backtesting.py
- Historical trade simulation on stored OHLCV data
- Trades logged to `backtest_trades.csv`
- Strictly candle-close based (no lookahead bias)

## Live Trading (Simulation)
- Executed on Binance Testnet
- Same strategy logic reused from backtesting module
- Trades logged to `live_trades.csv`
- Designed to maintain execution parity with backtests

## Validation
Backtest and live trades were compared based on:
- Trade direction
- Entry timing
- Execution price

Observed differences were minimal and primarily due to latency and market slippage, validating the deterministic architecture.

## Project Structure

