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


def exercise_3_2():
    """
    Use broadcasting to create beautiful color gradients.
    """
    print("\n" + "="*50)
    print("Exercise 3.2: Color Gradients with Broadcasting")
    print("="*50)
    # Create coordinate arrays
    width, height = 256, 256
    
    # TODO: Create x and y coordinate arrays using broadcasting
    # Hint: Create a column vector and row vector, then use broadcasting
    x = np.abs(np.linspace(-127,128,256)).reshape((256,1)) # Your code here - should be shape (256, 1)
    y = np.linspace(0,255,256).reshape((1,256)) # Your code here - should be shape (1, 256)
    
    # Create different gradient patterns using broadcasting
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    
    # Gradient 1: Linear horizontal
    gradient1 = x + np.zeros((1,256))
    
    # Gradient 2: Linear vertical
    gradient2 = y + np.zeros((256,1))
    
    # Gradient 3: Diagonal
    gradient3 = x + y
    
    # Gradient 4: Circular (distance from center)
    # TODO: Calculate distance from center (128, 128)
    center_x, center_y = 128, 128
    gradient4 = np.sqrt((x - center_x)**2 + (y - center_y)**2)
    
    # Gradient 5: Sine wave pattern
    gradient5 = np.sin(x * 0.1) * np.cos(y * 0.1)
    
    # Gradient 6: Your creative pattern!
    gradient6 = x % 37 + y % 21
    
    # Display all gradients
    gradients = [gradient1, gradient2, gradient3, gradient4, gradient5, gradient6]
    titles = ['Horizontal', 'Vertical', 'Diagonal', 'Circular', 'Sine Wave', 'Creative']
    for ax, grad, title in zip(axes.flat, gradients, titles):
        if grad is not None:
            ax.imshow(grad, cmap='viridis')
            ax.set_title(title)
            ax.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return gradients

# Run exercise 1_1
arrays = exercise_1_1()

# Create gradients (3_2)
exercise_3_2()