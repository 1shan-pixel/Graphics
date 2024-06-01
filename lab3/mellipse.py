import glfw
from OpenGL.GL import *
import math

def init_window(width, height):
    if not glfw.init():
        return None

    window = glfw.create_window(width, height, "Mid-point Ellipse Drawing", None, None)
    if not window:
        glfw.terminate()
        return None

    glfw.make_context_current(window)
    glOrtho(-width//2, width//2, -height//2, height//2, -1, 1)
    return window

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    
    glBegin(GL_POINTS)
    while (2 * ry**2 * x) <= (2 * rx**2 * y):
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        x += 1
        if p1 < 0:
            p1 += 2 * ry**2 * x + ry**2
        else:
            y -= 1
            p1 += 2 * ry**2 * x - 2 * rx**2 * y + ry**2
    
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    
    while y > 0:
        y -= 1
        glVertex2f(xc + x, yc + y)
        glVertex2f(xc - x, yc + y)
        glVertex2f(xc + x, yc - y)
        glVertex2f(xc - x, yc - y)
        if p2 > 0:
            p2 -= 2 * rx**2 * y + rx**2
        else:
            x += 1
            p2 += 2 * ry**2 * x - 2 * rx**2 * y + rx**2
    glEnd()

def main():
    window = init_window(800, 600)
    if not window:
        return

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        draw_ellipse(0, 0, 100, 50)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
