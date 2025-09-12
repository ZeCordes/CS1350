import numpy as np

def practice_6_student_gradebook():
    """
    Final Exercise: Complete Student Gradebook Analysis
    Use everything you've learned!
    """

    print("\n" + "="*50)
    print("FINAL PROJECT: Class Gradebook System")
    print("="*50)

    # Student grades: 6 students × 4 assignments
    grades = np.array([
        [88, 92, 85, 90], # Student 1
        [75, 80, 78, 82], # Student 2
        [93, 95, 91, 94], # Student 3
        [67, 70, 72, 68], # Student 4
        [82, 85, 88, 86], # Student 5
        [90, 88, 92, 89] # Student 6
        ])
    print("Class Gradebook:")
    print("Student HW1 HW2 HW3 HW4")
    for i in range(len(grades)):
        print(f" #{i+1} ", end="")
        for grade in grades[i]:
            print(f" {grade}", end="")
        print()
        
    # TODO 1: Calculate each student's average (per row)
    student_averages = np.mean(grades, axis=1)

    # TODO 2: Calculate each assignment's average (per column)
    assignment_averages = np.mean(grades, axis=0)

    # TODO 3: Find the highest grade in the class
    highest_grade = np.max(grades)

    # TODO 4: Count how many students have an average >= 85
    # First calculate student_averages, then use >= 85
    if student_averages is not None:    
        honor_roll = student_averages >= 85
        num_honor_roll = np.sum(honor_roll)

    # TODO 5: Add 5 bonus points to all grades (but cap at 100)
    curved_grades = np.minimum(grades + 5, 100)

    # Print your results
    print("\n--- ANALYSIS RESULTS ---")
    if student_averages is not None:
        print(f"Student averages: {student_averages}")
    if assignment_averages is not None:
        with np.printoptions(precision=2):
            print(f"Assignment averages: {assignment_averages}")
    if highest_grade is not None:
        print(f"Highest grade: {highest_grade}")
    if 'num_honor_roll' in locals() and num_honor_roll is not None:
        print(f"Students on honor roll: {num_honor_roll}")

    # Show letter grades
    if student_averages is not None:
        print("\n--- LETTER GRADES ---")
        for i, avg in enumerate(student_averages):
            if avg >= 90:
                letter = 'A'
            elif avg >= 80:
                letter = 'B'
            elif avg >= 70:
                letter = 'C'
            else:
                letter = 'D'
            print(f"Student #{i+1}: {avg:.1f} ({letter})")

# Run the final project
practice_6_student_gradebook()

print("\n" + " "*20)
print("CONGRATULATIONS! You've completed NumPy Statistical Functions!")
print("You can now:")
print("✓ Create and manipulate NumPy arrays")
print("✓ Calculate statistics (mean, max, min, sum)")
print("✓ Use universal functions for fast calculations")
print("✓ Work with 2D arrays (tables)")
print("✓ Filter and find specific values")
print("✓ Perform complete data analysis!")
print(" "*20)