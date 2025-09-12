import numpy as np

def practice_4b_grade_curve():
    """
    Exercise 4.2: Curving Grades
    Use ufuncs to adjust test scores
    """

    print("\n" + "="*50)
    print("EXERCISE 4.2: Grade Curving")
    print("="*50)

    # Test scores
    scores = np.array([65, 72, 78, 81, 69, 75, 83, 77, 70, 68])
    print("Original scores:", scores)

    # TODO 1: Add 10 points to all scores (curve)
    # Use: np.add(scores, 10) or scores + 10
    curved_scores = None # Replace None

    # TODO 2: Make sure no score exceeds 100
    # Use: np.minimum(curved_scores, 100)
    # This keeps the smaller of each score and 100
    capped_scores = None # Replace None
    
    # TODO 3: Calculate square root curve
    # Formula: new_score = sqrt(old_score) * 10
    # Use: np.sqrt(scores) * 10
    sqrt_curved = None # Replace None

    print(f"After +10 curve: {curved_scores}")
    print(f"Capped at 100: {capped_scores}")
    print(f"Square root curve: {sqrt_curved}")

# Run this exercise
practice_4b_grade_curve()