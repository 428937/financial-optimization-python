import numpy as np
from scipy.optimize import minimize

class PortfolioOptimizer:
    def optimize(self, expected_returns, cov_matrix):
        """Perform mean-variance optimization."""
        def objective(weights):
            port_return = np.dot(weights, expected_returns)
            port_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            return -port_return + 0.5 * port_risk ** 2

        n = len(expected_returns)
        bounds = [(0, 1) for _ in range(n)]
        constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        initial = np.array([1.0 / n] * n)

        result = minimize(objective, initial, bounds=bounds, constraints=constraints, method='SLSQP')
        return result.x if result.success else initial
