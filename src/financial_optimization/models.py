import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class LinearReturnModel:
    def __init__(self):
        self.models = {}

    def train(self, returns_data):
        for asset in returns_data.columns:
            df = returns_data[[asset]].copy()
            df['lag1'] = df[asset].shift(1)
            df = df.dropna()
            
            X = df[['lag1']].values
            y = df[asset].values
            
            if len(X) < 10:
                continue
                
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            self.models[asset] = model

    def predict_returns(self, returns_data):
        predictions = {}
        for asset, model in self.models.items():
            if asset in returns_data.columns:
                last_return = returns_data[asset].iloc[-1]
                pred = model.predict([[last_return]])[0]
                predictions[asset] = pred
        return predictions
