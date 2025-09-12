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
    # Find how many days were above 75°F
    hot_days = np.sum(temps >  75)

    # Find the temperatures on cool days (below 70°F)
    cool_temps = temps[temps < 70]

    # Find days with perfect weather (70-75°F)
    perfect_days = (temps >= 70) & (temps <= 75)
    num_perfect = sum(perfect_days)

    # Find the position of the hottest day
    hottest_day_index = np.argmax(temps)

    print(f"Days above 75°F: {hot_days}")
    print(f"Cool day temperatures: {cool_temps}")
    print(f"Number of perfect days: {num_perfect}")
    print(f"Hottest day was day #{hottest_day_index + 1 if hottest_day_index is not None else '?'}")

# Run this exercise
practice_5a_temperature_analysis()