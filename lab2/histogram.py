import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import bresenham.bresenham_less as bresenham

# Define number of bins
num_bins = 4
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Calculate histogram using numpy
hist, bin_edges = np.histogram(data, bins=num_bins)

# Define dimensions
hist_height = 400
hist_width = 800

# Determine the scaling factor
max_freq = max(hist)
scale_factor = hist_height / max_freq

# Define bar width
bar_width = hist_width // num_bins

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, hist_width, 0, hist_height, 0, 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, hist_width, 0, hist_height)

    glBegin(GL_POINTS)
    for i, frequency in enumerate(hist):
        bar_height = int(frequency * scale_factor)
        x0 = i * bar_width
        y0 = 0
        x1 = x0 + bar_width
        y1 = bar_height
        for x, y in bresenham(x0, y0, x0, y1):
            glVertex2f(x, y)
        for x, y in bresenham(x0, y1, x1, y1):
            glVertex2f(x, y)
        for x, y in bresenham(x1, y1, x1, y0):
            glVertex2f(x, y)
        for x, y in bresenham(x1, y0, x0, y0):
            glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(hist_width, hist_height, "Histogram", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
