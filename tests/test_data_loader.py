import unittest
from financial_optimization.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = DataLoader()
        tickers = ["AAPL"]
        data = loader.load_from_yfinance(tickers, start_date="2024-01-01")
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
