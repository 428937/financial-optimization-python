import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pandas as pd
from financial_optimization.data_loader import DataLoader
from financial_optimization.models import LinearReturnModel
from financial_optimization.optimizer import PortfolioOptimizer
from financial_optimization.utils import plot_portfolio_allocation

# Step 1: Define stockss
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Step 2: Load data using yfinance
loader = DataLoader()
prices = loader.load_from_yfinance(tickers)

print("Data loaded successfully. Shape:", prices.shape)

# Step 3: Calculate daily returns
returns = prices.pct_change().dropna()

# Step 4: Train Linear Regression models
model = LinearReturnModel()
model.train(returns)

# Step 5: Predict expected returns
expected_returns_dict = model.predict_returns(returns)
expected_returns = list(expected_returns_dict.values())

print("\nPredicted Expected Returns:")
for asset, ret in expected_returns_dict.items():
    print(f"{asset}: {ret:.4f}")

# Step 6: Calculate covariance matrix
cov_matrix = returns.cov()

# Step 7: Optimize portfolio
optimizer = PortfolioOptimizer()
weights = optimizer.optimize(expected_returns, cov_matrix.values)

print("\nOptimal Portfolio Weights:")
for ticker, weight in zip(tickers, weights):
    print(f"{ticker}: {weight:.4f} ({weight*100:.1f}%)")

# Step 8: Plot allocation
plot_portfolio_allocation(weights, tickers)
