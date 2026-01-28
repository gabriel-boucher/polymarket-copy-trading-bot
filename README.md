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

1. Clone the repository:
```bash
git clone https://github.com/yourusername/polymarket-copy-trading-bot.git
cd rpc-copy-trading-bot
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your configuration:
   - `POLYMARKET_API_KEY`: Your Polymarket API key
   - `POLYGON_RPC_URL`: Polygon RPC endpoint
   - `PRIVATE_KEY`: Your wallet private key (keep secure!)
   - `TARGET_WALLET_ADDRESS`: Wallet address to copy trades from

## Usage

Run the bot:
```bash
python -m app.main
```

### Trade Sizing Strategies

The bot supports three trade sizing strategies:

- **Fixed**: Always trade a fixed amount
- **Proportional**: Trade proportionally to the copied trader's position
- **Target**: Trade to match a target position size

Configure in your environment or config file.

## Project Structure

```
app/
├── application/        # Application services
├── config/            # Configuration management
├── domain/            # Domain models and business logic
├── infrastructure/    # External integrations (Polymarket, Polygon)
└── interfaces/        # API/CLI interfaces
```

## Development

### Type Checking

```bash
mypy app/
```

### Running Tests

```bash
pytest
```

## Security Warnings

⚠️ **IMPORTANT SECURITY NOTES:**
- Never commit your `.env` file or private keys
- Store private keys securely
- Use a dedicated wallet for bot trading
- Test with small amounts first
- Understand the risks of copy trading

## Disclaimer

This bot is for educational purposes. Trading cryptocurrencies and prediction markets carries risk. Use at your own risk. The authors are not responsible for any financial losses.

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
