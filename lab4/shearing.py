import glfw
from OpenGL.GL import *
import numpy as np

def init_window(width, height):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, "2D Shearing", None, None)
    if not window:
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    glOrtho(-width//2, width//2, -height//2, height//2, -1, 1)
    return window

def plot_shape(points):
    glBegin(GL_TRIANGLES)
    for point in points.T:
        glVertex2f(point[0], point[1])
    glEnd()

def shear(points, shx, shy):
    Sh = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0,  0, 1]
    ])
    return Sh @ points

def main():
    window = init_window(800, 600)
    if not window:
        return

    points = np.array([
        [0, 100, 50],
        [0, 0,  100],
        [1, 1,  1]
    ])

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Plot original shape
        glColor3f(1.0, 0.0, 0.0)  # Red
        plot_shape(points)

        # Sheared shape
        sheared_points = shear(points, 1, 0.5)
        glColor3f(0.0, 1.0, 0.0)  # Green
        plot_shape(sheared_points)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
