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

def translate(points, tx, ty):
    T = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0,  1]
    ])
    return T @ points

def rotate(points, theta):
    theta = np.radians(theta)
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,             0,             1]
    ])
    return R @ points

def scale(points, sx, sy):
    S = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])
    return S @ points

def reflect(points, axis):
    if axis == 'x':
        R = np.array([
            [1,  0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ])
    elif axis == 'y':
        R = np.array([
            [-1, 0, 0],
            [0,  1, 0],
            [0,  0, 1]
        ])
    elif axis == 'origin':
        R = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0,  0, 1]
        ])
    return R @ points

def shear(points, shx, shy):
    Sh = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0,  0, 1]
    ])
    return Sh @ points

def composite_transform(points, transformations):
    result = points
    for transform in transformations:
        result = transform(result)
    return result

def main():
    window = init_window(800, 600)
    if not window:
        return

    points = np.array([
        [0, 100, 100, 0],
        [0, 0,  100, 100],
        [1, 1,  1,  1]
    ])

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Plot original shape
        glColor3f(1.0, 0.0, 0.0)  # Red
        plot_shape(points)

        # Translated shape
        translated_points = translate(points, 200, 100)
        glColor3f(0.0, 1.0, 0.0)  # Green
        plot_shape(translated_points)

        # Rotated shape
        rotated_points = rotate(points, 45)
        glColor3f(0.0, 0.0, 1.0)  # Blue
        plot_shape(rotated_points)

        # Scaled shape
        scaled_points = scale(points, 2, 0.5)
        glColor3f(1.0, 1.0, 0.0)  # Yellow
        plot_shape(scaled_points)

        # Reflected shape
        reflected_points = reflect(points, 'y')
        glColor3f(0.0, 1.0, 1.0)  # Cyan
        plot_shape(reflected_points)

        # Sheared shape
        sheared_points = shear(points, 1, 0)
        glColor3f(1.0, 0.0, 1.0)  # Magenta
        plot_shape(sheared_points)

        # Composite transformation: translate, then rotate, then scale
        transformations = [
            lambda pts: translate(pts, 200, 100),
            lambda pts: rotate(pts, 45),
            lambda pts: scale(pts, 1.5, 1.5)
        ]
        composite_points = composite_transform(points, transformations)
        glColor3f(1.0, 1.0, 1.0)  # White
        plot_shape(composite_points)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
