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
    scores = np.array([65, 72, 78, 81, 69, 75, 83, 77, 70, 68, 94]) # added a 94 score to push one over 100 before capping
    print("Original scores:", scores)

    # Add 10 points to all scores (curve)
    curved_scores = scores + 10

    # Make sure no score exceeds 100
    # This keeps the smaller of each score and 100
    capped_scores = np.minimum(curved_scores, 100)
    
    # Calculate square root curve
    # Formula: new_score = sqrt(old_score) * 10
    sqrt_curved = (scores ** .5) * 10

    print(f"After +10 curve: {curved_scores}")
    print(f"Capped at 100: {capped_scores}")
    
    with np.printoptions(precision=2):
        print(f"Square root curve: {sqrt_curved}")

# Run this exercise
practice_4b_grade_curve()