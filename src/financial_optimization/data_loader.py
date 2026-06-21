import pandas as pd
import yfinance as yf

class DataLoader:
    def load_from_yfinance(self, tickers, start_date="2020-01-01"):
        """Download historical adjusted close prices using yfinance."""
        # Download data
        data = yf.download(tickers, start=start_date, progress=False, auto_adjust=False, threads=False)
        
        # Robust handling of yfinance output structure
        if isinstance(data.columns, pd.MultiIndex):
            # Multiple tickers → extract Adj Close level
            if 'Adj Close' in data.columns.get_level_values(0):
                prices = data['Adj Close']
            else:
                # Fallback to Close if Adj Close missing
                prices = data['Close']
        else:
            # Single ticker case
            if 'Adj Close' in data.columns:
                prices = data['Adj Close'].to_frame()
            elif 'Close' in data.columns:
                prices = data['Close'].to_frame()
            else:
                prices = data
        
        # Ensure proper column names (tickers)
        if isinstance(prices, pd.Series):
            prices = prices.to_frame()
        
        prices.columns = [col[1] if isinstance(col, tuple) else col for col in prices.columns]
        
        return prices
