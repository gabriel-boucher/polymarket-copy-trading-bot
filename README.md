# Polymarket Copy Trading Bot

A Python-based copy trading bot for Polymarket that monitors and replicates trades from specified wallet addresses.

## Features

- Monitor trades from target wallet addresses
- Automatically copy trades to your wallet
- Multiple trade sizing strategies (fixed, proportional, target-based)
- Clean architecture with domain-driven design
- Type-safe implementation with mypy

## Prerequisites

- Python 3.14 or higher
- A Polymarket account
- Polygon wallet with USDC

## Installation

Clone the repository:
```bash
git clone https://github.com/gabriel-boucher/polymarket-copy-trading-bot.git
cd polymarket-copy-trading-bot
```

Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## Configuration

Create a `.env` file in the root directory with the following variables:

### Required Environment Variables

```env
# Application Configuration
APP_START_TYPE=in_memory          # Options: "in_memory", "rpc"

# Wallet Addresses
USER_ADDRESS=                     # Your wallet address
TARGET_ADDRESS=                   # Target wallet address to copy trades from

# Wallet Private Key
USER_PRIVATE_KEY=                # Your wallet private key (keep secure!)

# Trade Sizing Strategy
TRADE_SIZE_STRATEGY=fixed         # Options: "fixed", "proportional", "same_as_target"
FIXED_TRADE_SIZE=5.0             # Fixed trade size in USDC (only used with "fixed" strategy)

# RPC Configuration (required when APP_START_TYPE=rpc)
INFURA_API_KEY=                  # Your Infura API key for Polygon RPC access
ALCHEMY_PRIVATE_KEY=             # Your Alchemy private key (alternative to Infura)
```

### Configuration Options

- **APP_START_TYPE**: 
  - `in_memory`: Uses in-memory repositories for testing
  - `rpc`: Uses live RPC connections to Polygon network

- **TRADE_SIZE_STRATEGY**:
  - `fixed`: Always trade a fixed amount (specified by FIXED_TRADE_SIZE)
  - `proportional`: Trade proportionally to the copied trader's balance and position
  - `same_as_target`: Match the exact trade size of the target wallet

## Usage

Run the bot:
```bash
python -m app.main
```

## Disclaimer

This bot is for educational purposes. Trading cryptocurrencies and prediction markets carries risk. Use at your own risk. The authors are not responsible for any financial losses.

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
