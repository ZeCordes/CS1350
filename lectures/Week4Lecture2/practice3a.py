import numpy as np

def practice_3a_sales_data():
    """
    Exercise 3.1: Store Sales Analysis
    Analyze weekly sales for different stores
    """
    
    print("\n" + "="*50)
    print("EXERCISE 3.1: Store Sales Data")
    print("="*50)
    
    # Sales data: 3 stores × 5 days (Monday-Friday)
    # Each row is a store, each column is a day
    sales = np.array([
        [100, 150, 120, 180, 200], # Store A
        [90, 110, 130, 160, 190], # Store B
        [120, 140, 110, 170, 210] # Store C
    ])

    print("Sales Data (rows=stores, columns=days):")
    print("Store A:", sales[0])
    print("Store B:", sales[1])
    print("Store C:", sales[2])

    # Calculate total sales for each store
    store_totals = np.sum(sales, axis=1)

    # Calculate average daily sales across all stores
    daily_averages = np.mean(sales)

    # Find the highest single day sales
    highest_sale = np.max(sales)

    # Calculate total sales for the entire week
    total_sales = np.sum(sales)
    
    print(f"\nStore totals: {store_totals}")
    print(f"Daily averages: {daily_averages}")
    print(f"Highest single day: ${highest_sale}")
    print(f"Total weekly sales: ${total_sales}")
    
    
practice_3a_sales_data()