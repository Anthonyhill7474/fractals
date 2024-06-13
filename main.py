import tkinter as tk
from euler import euler_formula
from mandelbrot import mandelbrot_fractal

def create_main_window():
    root = tk.Tk()
    root.title("Fractal Visualizer")

    label = tk.Label(root, text="Choose a fractal to visualize:")
    label.pack(pady=10)

    euler_button = tk.Button(root, text="Euler's Formula", command=euler_formula)
    euler_button.pack(pady=5)

    mandelbrot_button = tk.Button(root, text="Mandelbrot Fractal", command=mandelbrot_fractal)
    mandelbrot_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
