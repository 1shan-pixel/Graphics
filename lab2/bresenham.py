from OpenGL.GL import *
import glfw 

# for slope less than 1 , here we change the y parameter. 
def bresenham_less(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0
    for x in range(x0, x1 + 1):
        points.append((x, y))
        if D > 0:
            y = y + yi
            D = D - 2*dx
        D = D + 2*dy
    return points

#for slope greater than 1 , here we change the x parameter. 
def bresenham_more(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0
    for y in range(y0, y1 + 1):

        points.append((x, y))
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx
    return points


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) #this is the background color , that is black
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, 0.0, 1.0)

def display(window):
    glClear(GL_COLOR_BUFFER_BIT) #this is to clear the screen , that is to say , to make the background color appear. 

    # Render the points using Bresenham line drawing algorithms
    glBegin(GL_POINTS)
    for x, y in bresenham_less(0, 0, 10, 10):
        glVertex2f(x, y)
    for x, y in bresenham_more(0, 0, 10, 10):
        glVertex2f(x, y)
    glEnd()

    glfw.swap_buffers(window)

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create the window
    window = glfw.create_window(500, 500, "Bresenham Line Drawing", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Initialize the OpenGL context
    init()

    # Render loop
    while not glfw.window_should_close(window):
        display(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()

