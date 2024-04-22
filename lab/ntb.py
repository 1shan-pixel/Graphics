import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi

line_vertices = []

# Create 5 lines with decreasing lengths
for i in range(5):
    x_start = 0.0
    y_start = 0.5 - i * 0.1
    x_end = 0.8 - i * 0.16
    y_end = y_start
    line_vertices.extend([x_start, y_start, 0.0, x_end, y_end, 0.0])

def main():
    # Initialize GLFW
    if not glfw.init():
        print("Failed to initialize GLFW!")
        return

    # Create window
    window = glfw.create_window(640, 480, "Line Drawing", None, None)
    if not window:
        print("Failed to create GLFW window!")
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Create Vertex Array Object (VAO)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # Create Vertex Buffer Object (VBO)
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Upload vertex data to VBO
    glBufferData(GL_ARRAY_BUFFER, len(line_vertices) * sizeof(GLfloat), (GLfloat * len(line_vertices))(*line_vertices), GL_STATIC_DRAW)

    # Define vertex attribute pointer
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Main rendering loop
    while not glfw.window_should_close(window):
        # Clear the screen (optional)
        glClearColor(0.2, 0.3, 0.3, 1.0)  # Set background color (optional)
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the line
        glDrawArrays(GL_LINES, 0, len(line_vertices) // 3)

        # Swap buffers and poll events
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()


if __name__ == "__main__":
    main()