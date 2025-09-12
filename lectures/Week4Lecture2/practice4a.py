import numpy as np

def practice_4a_price_calculations():
    """
    Exercise 4.1: Store Price Calculations
    Use ufuncs to update prices
    """
    print("\n" + "="*50)
    print("EXERCISE 4.1: Price Updates with ufuncs")
    print("="*50)

    # Original prices
    prices = np.array([10.00, 25.50, 15.75, 30.00, 8.99])
    print("Original prices: $", prices)

    # TODO 1: Add 8% tax to all prices
    # Use: np.multiply(prices, 1.08) or prices * 1.08
    prices_with_tax = None # Replace None

    # TODO 2: Apply 20% discount (multiply by 0.8)
    # Use: np.multiply(prices, 0.8) or prices * 0.8
    discounted_prices = None # Replace None

    # TODO 3: Round all prices to nearest dollar
    # Use: np.round(prices)
    rounded_prices = None # Replace None

    # TODO 4: Find which prices are under $20
    # Use: np.less(prices, 20) or prices < 20
    under_20 = None # Replace None
    print(f"With 8% tax: ${prices_with_tax}")
    print(f"With 20% discount: ${discounted_prices}")
    print(f"Rounded prices: ${rounded_prices}")
    print(f"Under $20 (True/False): {under_20}")

# Run this exercise
practice_4a_price_calculations()