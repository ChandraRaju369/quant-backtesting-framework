# System Architecture – Multi-Timeframe Trading Strategy

## Overview
This system implements a deterministic multi-timeframe trading strategy using a unified architecture that ensures strict parity between backtesting and live execution. The same strategy logic is reused across both environments to guarantee reproducibility and eliminate inconsistencies.

## High-Level Architecture
The project follows a modular design with clear separation of concerns:

1. Data Layer  
2. Strategy Layer  
3. Execution Layer  
4. Logging & Validation Layer  

## 1. Data Layer
- Fetches historical OHLCV data from Binance REST API
- Supports multiple timeframes (15m and 1h)
- Stores data locally as CSV files
- Provides cleaned, structured input to the strategy engine
- Ensures candle-close based deterministic inputs

## 2. Strategy Layer (Core Logic)
- Single reusable strategy class
- Implements:
  - 15-minute SMA (9/21) crossover
  - 1-hour SMA (21) trend confirmation
- Deterministic decision-making at candle close
- No lookahead bias
- Same logic used for both backtest and live trading

## 3. Execution Layer
### Backtesting Execution
- Powered by backtesting.py framework
- Simulates trades using historical data
- Generates trade signals and execution logs
- Outputs stored in `backtest_trades.csv`

### Live Execution
- Integrated with Binance Testnet API
- Executes trades using identical strategy logic
- Handles order placement and execution tracking
- Outputs stored in `live_trades.csv`

## 4. Logging & Validation Layer
- Logs all trades with timestamp, price, and direction
- Compares backtest vs live trade outputs
- Validates:
  - Trade direction parity
  - Entry timing consistency
  - Price alignment
- Differences only due to latency and slippage

## Design Principles
- Deterministic execution (candle-close based)
- Code reusability (single strategy module)
- Reproducibility across environments
- Modular and extensible architecture
- Clear separation of data, logic, and execution

## Execution Flow
Data Ingestion → Strategy Signal Generation → Execution Engine → Trade Logging → Validation
