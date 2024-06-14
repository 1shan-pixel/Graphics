import glfw
from OpenGL.GL import *
import numpy as np

def init_window(width, height):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, "2D Transformations", None, None)
    if not window: 
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    glOrtho(-width//2, width//2, -height//2, height//2, -1, 1)
    return window

def plot_shape(points):
    glBegin(GL_LINE_LOOP) 
    for point in points.T:
        glVertex2f(point[0], point[1])
    glEnd()

def translate_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0,  1]
    ])

def rotate_matrix(theta):
    theta = np.radians(theta)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,             0,             1]
    ])

def scale_matrix(sx, sy):
    return np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])

def reflect_matrix(axis):
    if axis == 'x':
        return np.array([
            [1,  0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ])
    elif axis == 'y':
        return np.array([
            [-1, 0, 0],
            [0,  1, 0],
            [0,  0, 1]
        ])
    elif axis == 'origin':
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ])

def shear_matrix(shx, shy):
    return np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0,  0, 1]
    ])

def composite_transform_matrix(transformations):
    composite_matrix = np.eye(3)
    for transform in transformations:
        composite_matrix = transform @ composite_matrix
    return composite_matrix

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

        # Composite transformation: translate, then rotate, then scale
        transformations = [
            translate_matrix(50, 50),
            rotate_matrix(45),
            scale_matrix(1.5, 1.5)
        ]
        composite_matrix = composite_transform_matrix(transformations)
        composite_points = composite_matrix @ points
        glColor3f(1.0, 1.0, 1.0)  # White
        plot_shape(composite_points)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
