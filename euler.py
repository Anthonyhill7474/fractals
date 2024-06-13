import numpy as np
import matplotlib.pyplot as plt

def euler_formula():
    # Define the range of x values
    x = np.linspace(0, 2 * np.pi, 1000)

    # Euler's formula components
    real_part = np.cos(x)
    imaginary_part = np.sin(x)

    # Plot the complex exponential
    plt.figure(figsize=(8, 8))
    plt.plot(real_part, imaginary_part, label=r'$e^{ix} = \cos(x) + i\sin(x)$')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.title("Visualization of Euler's Formula")
    plt.show()
