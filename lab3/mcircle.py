import glfw
from OpenGL.GL import *
import math

def init_window(width, height):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, "Mid-point Circle Drawing", None, None)
    if not window:
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    glOrtho(-width//2, width//2, -height//2, height//2, -1, 1)
    return window

def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    
    glBegin(GL_POINTS)
    while x <= y:
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        glVertex2f(xc + y, yc + x)
        glVertex2f(xc - y, yc + x)
        glVertex2f(xc + y, yc - x)
        glVertex2f(xc - y, yc - x)
        
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        x += 1
    glEnd()

def main():
    window = init_window(800, 600)
    if not window:
        return

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        draw_circle(0, 0, 100)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
