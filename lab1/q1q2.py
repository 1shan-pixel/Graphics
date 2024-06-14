'''
Q1 
The programming language I am using this semester for performing my Computer Graphics Lab and Project is Python.
The Graphics Library I am using is PyOpenGL, which is a Python binding to the OpenGL API.

'''





''''

Q2

'''

import glfw #graphics library framework 
from OpenGL.GL import *
from OpenGL.GLU import * #OpenGl utility framework 

# Initialize GLFW
if not glfw.init():
    print("Failed to initialize GLFW!")

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(800, 600, "Graphics Environment", None, None) # for window and share , the last two args
if not window:
    print("Failed to create window!")
    glfw.terminate()

glfw.make_context_current(window)

# Initialize OpenGL
glClearColor(0.2, 0.3, 0.4, 1.0)  # Set the clear color to a pale blue
glMatrixMode(GL_PROJECTION)
glLoadIdentity() #ensures previous trans dont affect this one 
gluOrtho2D(0, 800, 0, 600)  # Set up an orthographic projection

# Get the display resolution using GLFW
monitor = glfw.get_primary_monitor()
mode = glfw.get_video_mode(monitor) #gets resolution and refresh rate
width, height = mode.size

print("Display resolution:", width, "x", height)

# Loop until the user closes the window
while not glfw.window_should_close(window):
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT) #clears the color buffers previously set

    # Swap buffers and poll for events
    glfw.swap_buffers(window) #prevent flickering
    glfw.poll_events()

glfw.terminate()