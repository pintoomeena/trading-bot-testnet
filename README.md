# Binance Futures Testnet Trading Bot

## Overview
This project is a CLI-based Python trading bot that places BUY and SELL
MARKET and LIMIT orders on **Binance USDT-M Futures Testnet**.
It demonstrates clean API integration, input validation, structured logging,
and a modular Python codebase.

> ⚠️ This project uses **Binance Futures Testnet (Demo Trading)**.  
> No real funds are used.

---

## Features
- Binance USDT-M Futures Testnet integration
- BUY / SELL orders
- MARKET and LIMIT order types
- Command-line interface (CLI)
- Input validation and error handling
- Structured file-based logging
- Modular and readable project structure

---

## Project Structure
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── cli.py
├── requirements.txt
├── README.md
└── logs/
    └── trading_bot.log