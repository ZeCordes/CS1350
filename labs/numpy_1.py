# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import time

# Set up matplotlib for inline display (if using Jupyter)
# For regular Python, plots will open in separate windows
plt.style.use('seaborn-v0_8-darkgrid') # Make plots look nice!

# Set random seed for reproducibility
np.random.seed(42)

print("Lab environment ready!")
print(f"NumPy version: {np.__version__}")

def exercise_1_1():
    """
    Create arrays using different methods and visualize them.
    """
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)
    
    # TODO: Create the following arrays
    # 1. An array of integers from 0 to 20
    array_range = np.arange(21) # Your code here
    
    # 2. An array of 50 evenly spaced points between 0 and 2π
    array_linear = np.linspace(0, np.pi*2, 50) # Your code here
    
    # 3. A 5x5 identity matrix
    identity_matrix = np.identity(5) # Your code here
    
    # 4. A 3x3 matrix filled with random integers between 1 and 10
    random_matrix = np.random.randint(0, 11, (3, 3)) # Your code here
    
    # Visualization (provided)
    if array_range is not None and array_linear is not None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        # Plot 1: Bar chart of range array
        axes[0, 0].bar(range(len(array_range)), array_range, color='skyblue')
        axes[0, 0].set_title('Array Range (0 to 20)')
        axes[0, 0].set_xlabel('Index')
        axes[0, 0].set_ylabel('Value')
        
        # Plot 2: Sine wave using linear space
        if array_linear is not None:
            sine_wave = np.sin(array_linear)
            axes[0, 1].plot(array_linear, sine_wave, 'b-', linewidth=2)
            axes[0, 1].set_title('Sine Wave')
            axes[0, 1].set_xlabel('Radians')
            axes[0, 1].set_ylabel('sin(x)')
            axes[0, 1].grid(True)
        
        # Plot 3: Identity matrix as heatmap
        if identity_matrix is not None:
            im = axes[1, 0].imshow(identity_matrix, cmap='RdBu', vmin=0, vmax=1)
            axes[1, 0].set_title('5x5 Identity Matrix')
            plt.colorbar(im, ax=axes[1, 0])
        
        # Plot 4: Random matrix as heatmap
        if random_matrix is not None:
            im = axes[1, 1].imshow(random_matrix, cmap='viridis')
            axes[1, 1].set_title('3x3 Random Matrix')
            for i in range(3):
                for j in range(3):
                    axes[1, 1].text(j, i, f'{random_matrix[i, j]}',
                        ha='center', va='center', color='white')
            plt.colorbar(im, ax=axes[1, 1])
        
        
        plt.tight_layout()
        plt.show()
        
        return array_range, array_linear, identity_matrix, random_matrix


# Run the exercise
arrays = exercise_1_1()