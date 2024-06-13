import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_fractal():
    # Generate Mandelbrot set
    width, height = 800, 800
    mandelbrot_set = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = 3.5 * (x - width / 2) / (width / 2)
            imag = 2.0 * (y - height / 2) / (height / 2)
            c = complex(real, imag)
            mandelbrot_set[x, y] = mandelbrot(c, 256)

    plt.imshow(mandelbrot_set.T, cmap='hot', extent=[-2, 1, -1, 1])
    plt.colorbar()
    plt.title("Mandelbrot Fractal")
    plt.show()
