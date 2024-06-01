import glfw
from OpenGL.GL import *
import numpy as np

def init_window(width, height):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, "Sutherland-Hodgman Polygon Clipping", None, None)
    if not window:
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    glOrtho(-width//2, width//2, -height//2, height//2, -1, 1)
    return window

def plot_polygon(vertices, color):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def inside(point, edge_start, edge_end):
    return (edge_end[0] - edge_start[0]) * (point[1] - edge_start[1]) > (edge_end[1] - edge_start[1]) * (point[0] - edge_start[0])

def compute_intersection(start, end, edge_start, edge_end):
    dx1, dy1 = end[0] - start[0], end[1] - start[1]
    dx2, dy2 = edge_end[0] - edge_start[0], edge_end[1] - edge_start[1]
    determinant = dx1 * dy2 - dy1 * dx2
    if determinant == 0:
        return None
    t = ((start[0] - edge_start[0]) * dy2 - (start[1] - edge_start[1]) * dx2) / determinant
    return (start[0] + t * dx1, start[1] + t * dy1)

def sutherland_hodgman(polygon, clip_window):
    clipped_polygon = polygon
    for i in range(len(clip_window)):
        edge_start = clip_window[i]
        edge_end = clip_window[(i + 1) % len(clip_window)]
        new_polygon = []
        for j in range(len(clipped_polygon)):
            start = clipped_polygon[j]
            end = clipped_polygon[(j + 1) % len(clipped_polygon)]
            if inside(end, edge_start, edge_end):
                if not inside(start, edge_start, edge_end):
                    new_polygon.append(compute_intersection(start, end, edge_start, edge_end))
                new_polygon.append(end)
            elif inside(start, edge_start, edge_end):
                new_polygon.append(compute_intersection(start, end, edge_start, edge_end))
        clipped_polygon = new_polygon
    return clipped_polygon

def main():
    window = init_window(800, 600)
    if not window:
        return

    polygon = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
    clip_window = [(-50, -50), (150, -50), (150, 100), (-50, 100)]

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Plot clipping window
        plot_polygon(clip_window, (0.0, 0.0, 1.0))  # Blue

        # Plot original polygon
        plot_polygon(polygon, (1.0, 0.0, 0.0))  # Red

        # Plot clipped polygon
        clipped_polygon = sutherland_hodgman(polygon, clip_window)
        if clipped_polygon:
            plot_polygon(clipped_polygon, (0.0, 1.0, 0.0))  # Green

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
