import numpy as np

def practice_5a_temperature_analysis():
    """
    Exercise 5.1: Temperature Analysis
    Find specific temperature conditions
    """

    print("\n" + "="*50)
    print("EXERCISE 5.1: Finding Temperature Patterns")
    print("="*50)

    # Daily temperatures for two weeks
    temps = np.array([68, 72, 75, 71, 80, 82, 79,
        77, 73, 70, 69, 74, 78, 76])

    print("Two weeks of temperatures:", temps)
    # TODO 1: Find how many days were above 75°F
    # Use: np.sum(temps > 75)
    hot_days = None # Replace None

    # TODO 2: Find the temperatures on cool days (below 70°F)
    # Use: temps[temps < 70]
    cool_temps = None # Replace None

    # TODO 3: Find days with perfect weather (70-75°F)
    # Use: (temps >= 70) & (temps <= 75)
    perfect_days = None # Replace None
    num_perfect = None # Use np.sum on perfect_days

    # TODO 4: Find the position of the hottest day
    # Use: np.argmax(temps)
    hottest_day_index = None # Replace None

    print(f"Days above 75°F: {hot_days}")
    print(f"Cool day temperatures: {cool_temps}")
    print(f"Number of perfect days: {num_perfect}")
    print(f"Hottest day was day #{hottest_day_index + 1 if hottest_day_index is not None else '?'}")

# Run this exercise
practice_5a_temperature_analysis()