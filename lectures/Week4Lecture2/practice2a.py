import numpy as np

def practice_2a_basic_stats():
    """
    Exercise 2.1: Calculate Basic Statistics
    Let's analyze homework scores!
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: Homework Score Statistics")
    print("="*50)
    
    # Here are homework scores (out of 100)
    homework_scores = np.array([85, 92, 78, 95, 88, 73, 90, 82, 87, 91])
    print("Homework scores:", homework_scores)

    # TODO 1: Calculate the average score
    # Use: np.mean(homework_scores)
    average = None # Replace None with your calculation

    # TODO 2: Find the highest score
    # Use: np.max(homework_scores)
    highest = None # Replace None with your calculation

    # TODO 3: Find the lowest score
    # Use: np.min(homework_scores)
    lowest = None # Replace None with your calculation

    # TODO 4: Calculate total points earned
    # Use: np.sum(homework_scores)
    total = None # Replace None with your calculation
    
    print(f"Average score: {average}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Total points: {total}")
    
    # Bonus: How many students scored above 85?
    above_85 = homework_scores > 85 # This creates True/False array
    count_above_85 = np.sum(above_85) # True counts as 1, False as 0
    print(f"Students scoring above 85: {count_above_85}")
    
# Run this exercise
practice_2a_basic_stats()