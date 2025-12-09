def get_file_stats(filename):
    """
    Get statistics about a text file.

    Parameters:
        filename (str): Name of the file to analyze
    
    Returns:
        dict: Dictionary with 'lines', 'words', and 'characters' counts
        Returns None if file doesn't exist
    
    Example:
        If file contains:
        "Hello world
        Python is great"
    
        get_file_stats("file.txt") returns:
        {'lines': 2, 'words': 5, 'characters': 26}
    """
    
    # YOUR CODE HERE
    # Hint: Use try-except for file handling
    # Hint: Use readlines() to get all lines
    # Hint: Use split() to count words
    # Hint: Use len() for character count
    
    try:
        with open(filename, 'r') as file:
            full_contents = file.read()
            file.seek(0) # reset cursor for readlines
            return {
                'lines': len(file.readlines()),
                'words': len(full_contents.split()),
                'characters': len(full_contents)
            }
    except FileNotFoundError:
        return None


def test_one():
    stats = get_file_stats("final_test_file.txt")
    if stats:
        print(f"Lines: {stats['lines']}")
        print(f"Words: {stats['words']}")
        print(f"Characters: {stats['characters']}")




class Student:
    """
    A class to represent a student and their grades.
    """

    def __init__(self, name, student_id):
        """
        Initialize a student with name and ID.
        Start with an empty list of grades.
        Parameters:
        name (str): Student's name
        student_id (str): Student's ID number
        """
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade: float) -> bool:
        """
        Add a grade to the student's record.
        Only add if grade is between 0 and 100.
        Parameters:
        grade (float): Grade to add
        Returns:
        bool: True if grade was added, False otherwise
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        
        return False

    def calculate_average(self) -> float:
        """
        Calculate the student's average grade.
        Returns:
        float: Average of all grades
        Returns 0 if no grades exist
        """
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0.0

    def get_status(self) -> str:
        """
        Get student's pass/fail status.
        Returns:
        str: "Passing" if average >= 70, "Failing" otherwise
        "No grades" if no grades recorded
        """
        return "Passing" if self.calculate_average() >= 70 else "Failing" if len(self.grades) > 0 else "No grades"


def test_two():
    student = Student("Alice", "12345")
    print(student.add_grade(85)) # Should print: True
    print(student.add_grade(92)) # Should print: True
    print(student.add_grade(150)) # Should print: False
    print(student.calculate_average()) # Should print: 88.5
    print(student.get_status()) # Should print: "Passing"




def safe_get_element(my_list, index, default_value=None):
    """
    Safely get an element from a list at the given index.
    Parameters:
        my_list: List to access (might not be a list!)
        index: Index to access (might not be valid!)
        default_value: Value to return if access fails
    
    Returns:
        Element at index if successful
        default_value if any error occurs
    
    Examples:
        safe_get_element([1, 2, 3], 1, -1) returns 2
        safe_get_element([1, 2, 3], 10, -1) returns -1
        safe_get_element("not a list", 0, -1) returns -1
        safe_get_element([1, 2, 3], "bad", -1) returns -1
    """

    try:
        return my_list.index(index) # use .index so it only proccesses lists
    except Exception: # no different logic for index or type error so catch alongside other errors
        return default_value

def test_three():
    print(safe_get_element([1, 2, 3], 1)) # 2
    print(safe_get_element([1, 2, 3], 10, -1)) # -1
    print(safe_get_element("not list", 0, -1)) # -1
    print(safe_get_element([1, 2, 3], "bad", -1)) # -1




def recursive_power(x: int|float, n: int):
    if n % 1 != 0 or n < 0:
        raise ValueError
    
    if n == 0:
        return 1
    else:
        return x * recursive_power(x, n - 1)


def test_four():
    print(recursive_power(2, 3)) # 8
    print(recursive_power(5, 2)) # 25
    print(recursive_power(10, 0)) # 1
    print(recursive_power(3, 4)) # 81



def analyze_sales(sales_data: list[dict[str, int|float]]):
    """
    Analyze sales data using map, filter, and lambda functions.
    
    Parameters:
        sales_data: List of dictionaries with 'product', 'quantity', 'price'
    
    Returns:
        Dictionary with:
            - 'total_revenue': Sum of all sales (quantity * price)
            - 'high_value': List of products with revenue > 100
            - 'low_stock': List of products with quantity < 10
            - 'average_price': Average price of all products
    
    Example:
        sales_data = [
            {'product': 'Widget', 'quantity': 5, 'price': 25.00},
            {'product': 'Gadget', 'quantity': 15, 'price': 10.00},
            {'product': 'Tool', 'quantity': 3, 'price': 50.00}
        ]

        Returns:
        {
            'total_revenue': 425.0,
            'high_value': ['Widget', 'Gadget', 'Tool'],
            'low_stock': ['Widget', 'Tool'],
            'average_price': 28.33
        }
    """
    
    # Step 1: Calculate revenue for each item
    # Add 'revenue' key to each dictionary
    # Hint: revenue = quantity * price
    with_revenue = list(map(lambda product_dict: {**product_dict, **{'revenue': product_dict['quantity'] * product_dict['price']}}, sales_data)) # this is messy

    # Step 2: Calculate total revenue
    total_revenue = sum(map(lambda product_dict: product_dict['revenue'], with_revenue))
    
    # Step 3: Filter high-value items (revenue > 100)
    high_value_items = filter(lambda product_dict: product_dict['revenue'] > 100, with_revenue)
    
    # Step 4: Filter low-stock items (quantity < 10)
    low_stock_items = filter(lambda product_dict: product_dict['quantity'] < 10, with_revenue)
    
    # Step 5: Calculate average price
    average_price = sum(map(lambda product_dict: product_dict['price'], with_revenue)) / len(with_revenue)

    return {
        'total_revenue': total_revenue,
        'high_value': [item['product'] for item in high_value_items],
        'low_stock': [item['product'] for item in low_stock_items],
        'average_price': round(average_price, 2) if sales_data else 0
    }

def test_five():
    test_sales = [
        {'product': 'Widget', 'quantity': 5, 'price': 25.00},
        {'product': 'Gadget', 'quantity': 15, 'price': 10.00},
        {'product': 'Tool', 'quantity': 3, 'price': 50.00},
        {'product': 'Device', 'quantity': 20, 'price': 5.00}
    ]
    result = analyze_sales(test_sales)
    print(result)


test_one()
print('-----')

test_two()
print('-----')

test_three()
print('-----')

test_four()
print('-----')

test_five()