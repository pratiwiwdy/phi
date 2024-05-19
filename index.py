import matplotlib.pyplot as plt
import numpy as np

def visualize_golden_ratio():
    # Golden Ratio
    phi = (1 + np.sqrt(5)) / 2

    # Create a figure and a set of subplots
    fig, ax = plt.subplots()

    # Create a rectangle representing 1
    rectangle1 = plt.Rectangle((0, 0), 1, 1, fill=False)
    ax.add_patch(rectangle1)

    # Create a square representing phi-1 (which is 1/phi)
    square = plt.Rectangle((1, 0), 1/phi, 1/phi, fill=False, color='r')
    ax.add_patch(square)

    # Create a rectangle representing phi
    rectangle2 = plt.Rectangle((0, 0), phi, 1, fill=False, color='b')
    ax.add_patch(rectangle2)

    # Set the limits of the plot from -0.5 to 2 in x-axis and -0.5 to 1.5 in y-axis
    plt.xlim(-0.5, 2)
    plt.ylim(-0.5, 1.5)

    # Set the title of the plot
    plt.title('Visualization of Golden Ratio (Phi)')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    visualize_golden_ratio()
