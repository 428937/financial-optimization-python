# Financial Optimization with Python

A Python project for **financial portfolio optimization** using real stock data from **yfinance**. 
The project focuses heavily on **Linear Regression** to predict expected returns for each asset, which are then used in a **Mean-Variance Optimization** (Markowitz-style) to find the best portfolio allocation.

Perfect for learning how to combine machine learning (Linear Regression) with financial optimization in a clean, understandable way.

---

## Features

- **Real-time data**: Downloads historical stock prices using `yfinance`
- **Linear Regression Models**: Trains one model per stock using lagged returns as features
- **Portfolio Optimization**: Mean-variance optimization with SciPy
- **Visualization**: Automatic pie chart showing optimal allocation
- **Highly Modular**: Easy to extend (add new models, constraints, features, etc.)
- **Clear Structure**: Well-organized package for learning and scaling
- **Detailed Example**: Step-by-step walkthrough in the main script

---

## Project Structure

```
financial-optimization-python/
├── README.md                    # This file
├── requirements.txt             # Project dependencies
├── src/
│   └── financial_optimization/  # Main Python package
│       ├── __init__.py          # Package exports
│       ├── data_loader.py       # Handles data downloading
│       ├── models.py            # Linear Regression prediction models
│       ├── optimizer.py         # Portfolio optimization logic
│       └── utils.py             # Helper functions (plotting, etc.)
├── examples/
│   └── basic_portfolio_optimization.py  # Complete working example
└── tests/
    └── test_data_loader.py      # Basic unit tests
```

---

## Installation

### 1. Clone or Download the Repository

```bash
git clone https://github.com/428937/financial-optimization-python.git
cd financial-optimization-python
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies**:
- `yfinance` — Stock data
- `pandas` & `numpy` — Data handling
- `scikit-learn` — Linear Regression
- `scipy` — Optimization
- `matplotlib` — Visualization

---

## Quick Start

1. Open a terminal in the project folder.
2. Run the example:

```bash
cd examples
python basic_portfolio_optimization.py
```

**What you will see**:
- Confirmation that data was downloaded
- Predicted expected returns from Linear Regression models
- Optimal portfolio weights
- A pie chart showing the recommended allocation

---

## How It Works

### 1. Data Loading (`data_loader.py`)
- Downloads adjusted close prices for chosen stocks using `yfinance`
- Example tickers: AAPL, MSFT, GOOGL, AMZN

### 2. Feature Engineering & Linear Regression (`models.py`)
- Computes daily returns
- Creates lagged return features
- Trains a separate **Linear Regression** model for each stock
- Predicts next-period expected return for each asset

### 3. Risk Modeling
- Builds the covariance matrix from historical returns (measures risk/correlations)

### 4. Portfolio Optimization (`optimizer.py`)
- Uses **Mean-Variance Optimization** to maximize return for a given risk level
- Constraints: weights between 0 and 1, sum to 100%

### 5. Visualization (`utils.py`)
- Displays the optimal portfolio as a pie chart

---

## Example Output

```text
Data loaded successfully. Shape: (1624, 4)

Predicted Expected Returns:
AAPL: 0.0007
AMZN: -0.0003
GOOGL: 0.0007
MSFT: 0.0006

Optimal Portfolio Weights:
AAPL: 0.3253 (32.5%)
MSFT: 0.0000 (0.0%)
GOOGL: 0.3127 (31.3%)
AMZN: 0.3621 (36.2%)
```

*(A pie chart window will also pop up)*

<img width="1266" height="1102" alt="image" src="https://github.com/user-attachments/assets/4dc8ef75-3632-4b5f-b266-2e0eab59f779" />


---

## Customization Ideas

- Change tickers in `basic_portfolio_optimization.py`
- Add more features to Linear Regression (volume, moving averages, market index, etc.)
- Add risk-free rate or different optimization objectives
- Implement backtesting
- Add more advanced models (Random Forest, LSTM, etc.)

---

## Running Tests

```bash
python -m pytest tests/ -v
```

or

```bash
python -m unittest tests/test_data_loader.py
```

---

## Project Philosophy

This project was built with **clarity and modularity** in mind:
- Short, focused modules
- Minimal comments inside code (explanations are in README and file structure)
- Easy to read and modify
- Strong emphasis on **Linear Regression** as requested
