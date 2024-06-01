import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 10
BALL_SPEED = 5

# Initialize Pygame
pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)

# Set up OpenGL
gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
glClearColor(0, 0, 0, 1)

# Define paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + PADDLE_WIDTH, self.y)
        glVertex2f(self.x + PADDLE_WIDTH, self.y + PADDLE_HEIGHT)
        glVertex2f(self.x, self.y + PADDLE_HEIGHT)
        glEnd()

    def move_up(self):
        if self.y < WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.y += PADDLE_SPEED

    def move_down(self):
        if self.y > 0:
            self.y -= PADDLE_SPEED

# Define ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + BALL_SIZE, self.y)
        glVertex2f(self.x + BALL_SIZE, self.y + BALL_SIZE)
        glVertex2f(self.x, self.y + BALL_SIZE)
        glEnd()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x + BALL_SIZE >= WINDOW_WIDTH:
            self.dx *= -1
        if self.y <= 0 or self.y + BALL_SIZE >= WINDOW_HEIGHT:
            self.dy *= -1

        # Handle paddle collision
        if (self.x <= left_paddle.x + PADDLE_WIDTH and 
            self.y + BALL_SIZE >= left_paddle.y and 
            self.y <= left_paddle.y + PADDLE_HEIGHT):
            self.dx *= -1

        if (self.x + BALL_SIZE >= right_paddle.x and 
            self.y + BALL_SIZE >= right_paddle.y and 
            self.y <= right_paddle.y + PADDLE_HEIGHT):
            self.dx *= -1

# Create paddles and ball objects
left_paddle = Paddle(20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(WINDOW_WIDTH - 20 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2)

# Main game loop
while True:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        left_paddle.move_up()
    if keys[K_s]:
        left_paddle.move_down()
    if keys[K_UP]:
        right_paddle.move_down()
    if keys[K_DOWN]:
        right_paddle.move_up()

    ball.move()

    left_paddle.draw()
    right_paddle.draw()
    ball.draw()

    pygame.display.flip()
    pygame.time.wait(10)
