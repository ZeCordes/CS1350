import numpy as np

def practice_2b_shopping_analysis():
    
    """
    Exercise 2.2: Shopping Cart Analysis
    Let's analyze shopping data!
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: Shopping Cart Analysis")
    print("="*50)

    # Prices of items in a shopping cart
    item_prices = np.array([5.99, 12.50, 3.25, 8.75, 15.00, 7.50, 4.99, 9.99])
    print("Item prices: $", item_prices)

    # Calculate total cost
    total_cost = np.sum(item_prices)

    # Find the most expensive item
    most_expensive = np.max(item_prices)

    # Find the cheapest item
    cheapest = np.min(item_prices)

    # Calculate average item price
    average_price = np.mean(item_prices)
    
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Most expensive item: ${most_expensive:.2f}")
    print(f"Cheapest item: ${cheapest:.2f}")
    print(f"Average item price: ${average_price:.2f}")

    # Bonus: Apply 10% discount to all items
    discounted = item_prices * 0.9
    savings = total_cost - np.sum(discounted) if total_cost else 0
    print(f"After 10% discount, you save: ${savings:.2f}")

# Run this exercise
practice_2b_shopping_analysis()