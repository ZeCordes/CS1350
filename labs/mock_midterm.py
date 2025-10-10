""" Problem 1: Restaurant Order System
Create a restaurant order system with these functions:
1. add_to_order(order, item_name, quantity, price_per_item)
    - Add item to order (or update quantity if exists)
    - quantity must be positive integer
    - price must be positive number
    - Return True if successful, False otherwise

2. remove_from_order(order, item_name)
    - Remove item completely from order
    - Return True if removed, False if item not found

3. calculate_bill(order, tax_rate)
    - Calculate total bill including tax
    - tax_rate is percentage (e.g., 8 for 8%)
    - Return total amount
    *bonus*

4. get_most_expensive_item(order)
    - Find item with highest total cost (price * quantity)
    - Return item name, or None if order is empty

Example:
    order = {}
    add_to_order(order, "Pizza", 2, 12.99)
    add_to_order(order, "Soda", 3, 2.50)
    
    bill = calculate_bill(order, 8) # 8% tax
    print(f"Total: ${bill:.2f}")
"""

def add_to_order(order: dict[str, tuple[int, float]], item_name: str, quantity: int, price_per_item: float) -> bool:
    # operates in-place
    if quantity <= 0 or price_per_item <= 0:
        return False
    
    order[item_name] = (quantity, price_per_item)
    return True

def remove_from_order(order: dict[str, tuple[int, float]], item_name: str) -> bool:
    # operates in-place
    if item_name in order:
        del order[item_name]
        return True
    else:
        return False

def calculate_bill(order: dict[str, tuple[int, float]], tax_rate: int|float) -> float:
    return sum(quantity * price for quantity, price in order.values()) * (1 + (tax_rate / 100))

def get_most_expensive_item(order: dict[str, tuple[int, float]]) -> str|None:
    return max(order.keys(), key = lambda item_name: order[item_name][0] * order[item_name][1])

# Test your functions
if __name__ == "__main__":
    print("-----Problem 1: Restaurant Order System-----")
    order = {}
    # Test adding items
    print(add_to_order(order, "Burger", 2, 8.99)) # True
    print(add_to_order(order, "Fries", -1, 3.50)) # False (negative quantity)
    print(add_to_order(order, "Drink", 2, 2.99)) # True
    print(f"Order: {order}")
    # Test bill calculation
    total = calculate_bill(order, 10) # 10% tax
    print(f"Total with 10% tax: ${total:.2f}")
    # Test most expensive
    # bonus
    expensive = get_most_expensive_item(order)
    print(f"Most expensive item: {expensive}")
    # Test removal
    print(remove_from_order(order, "Drink")) # True
    print(remove_from_order(order, "Pizza")) # False (not in order)





""" Problem 2: Movie Theater Seating
Track movie theater seat reservations using sets.

Write these functions:
1. reserve_seats(reservations, movie_name, seat_numbers)
    - Reserve seats for a movie
    - reservations: dict where keys are movie names, values are sets of reserved
    seats
    - seat_numbers: list of seat numbers to reserve
    - Add movie if doesn't exist

2. cancel_reservation(reservations, movie_name, seat_numbers)
    - Cancel specific seat reservations
    - Return True if cancelled, False if movie doesn't exist

3. get_available_seats(reservations, movie_name, total_seats)
    - Find available seats (not reserved)
    - total_seats: set of all seat numbers in theater
    - Return set of available seats

4. find_common_viewers(reservations, movie1, movie2)
    - Find seats (people) who reserved both movies
    - Assume same seat number = same person
    - Return set of seat numbers

Example:
    reservations = {}
    reserve_seats(reservations, "Avatar", [1, 2, 3, 5])
    reserve_seats(reservations, "Inception", [2, 3, 6, 7])
    common = find_common_viewers(reservations, "Avatar", "Inception")
    print(common) # {2, 3} - seats 2 and 3 watched both
"""

def reserve_seats(reservations: dict, movie_name: str, seat_numbers: list[int]):
    # Your code here
    pass

def cancel_reservation(reservations: dict, movie_name: str, seat_numbers: list[int]):
    # Your code here
    pass

def get_available_seats(reservations, movie_name, total_seats):
    # Your code here
    pass

def find_common_viewers(reservations, movie1, movie2):
    # Your code here
    pass

"""
Analyze test scores for a class.

Write functions to:
1. create_random_scores(num_students, num_tests)
    - Generate random test scores between 50-100
    - Return 2D array (students x tests)

2. identify_failing_tests(scores, passing_grade)
    - Find which tests each student failed
    - Return 2D boolean array (True = failed)

3. calculate_student_ranks(scores)
    - Rank students by their average score
    - Return array of student indices sorted by average (highest first)

4. apply_curve(scores, curve_type, value)
    - Apply curve to all scores
    - curve_type: "add" (add points) or "multiply" (multiply by factor)
    - Cap scores at 100
    - Return curved scores

Example:
    scores = create_random_scores(5, 3) # 5 students, 3 tests
    print(scores)
    failing = identify_failing_tests(scores, 70)
    print(f"Failed tests: {failing}")
    ranks = calculate_student_ranks(scores)
    print(f"Student rankings: {ranks}")
"""

import numpy as np

# Write your code here:
def create_random_scores(num_students: int, num_tests: int):
    return np.random.randint(50, 100, (num_students, num_tests))

def identify_failing_tests(scores, passing_grade):
    return scores < passing_grade

def calculate_student_ranks(scores):
    return 

def apply_curve(scores, curve_type, value):
    # Your code here
    pass