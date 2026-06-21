import pandas as pd
import yfinance as yf

class DataLoader:
    def load_from_yfinance(self, tickers, start_date="2020-01-01"):
        """Download historical adjusted close prices."""
        data = yf.download(tickers, start=start_date, progress=False)['Adj Close']
        return data
