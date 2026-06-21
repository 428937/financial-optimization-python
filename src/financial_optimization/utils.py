import matplotlib.pyplot as plt

def plot_portfolio_allocation(weights, asset_names):
    """Plot pie chart of portfolio weights."""
    plt.figure(figsize=(8, 6))
    plt.pie(weights, labels=asset_names, autopct='%1.1f%%', startangle=90)
    plt.title('Optimal Portfolio Allocation')
    plt.axis('equal')
    plt.show()
