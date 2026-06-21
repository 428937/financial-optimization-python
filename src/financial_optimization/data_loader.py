import pandas as pd
import yfinance as yf

class DataLoader:
    def load_from_yfinance(self, tickers, start_date="2020-01-01"):
        """Download historical adjusted close prices."""
        data = yf.download(tickers, start=start_date, progress=False)
        
        # Fix for multi-ticker MultiIndex structure
        if isinstance(data.columns, pd.MultiIndex):
            data = data['Adj Close']
        else:
            # Single ticker case
            if 'Adj Close' in data.columns:
                data = data[['Adj Close']]
        
        return data
