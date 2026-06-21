import numpy as np
from scipy.optimize import minimize

class PortfolioOptimizer:
    def optimize(self, expected_returns, cov_matrix):
        expected_returns = np.array(list(expected_returns.values())) if isinstance(expected_returns, dict) else np.array(expected_returns)
        cov_matrix = np.array(cov_matrix)
        
        def objective(weights):
            port_return = np.dot(weights, expected_returns)
            port_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
            return -port_return + 2.0 * port_variance

        n = len(expected_returns)
        bounds = [(0.0, 1.0) for _ in range(n)]
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}
        initial = np.array([1.0 / n] * n)

        result = minimize(objective, initial, bounds=bounds, constraints=constraints, method='SLSQP')
        
        if result.success:
            return result.x
        else:
            print(f"Optimization failed: {result.message}")
            return initial
