import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

class Logo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
        self.clock = pygame.time.Clock()
        self.show_screen()
        
    def show_screen(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glOrtho(0, 1280, 720, 0, -1, 1)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glColor3f(10.0, 0.0, 0.0)
            draw_u_shape(x=300,y=100,width=50,height=150,space=90)
            # draw_shapes()
            draw_rectangle(400,300,50,350)
            # draw_u_shape(100, 100, 50,400,90)
            pygame.display.flip()
            self.clock.tick(60)
            

def draw_rectangle(x, y, width, height):
    # glBegin(GL_QUADS)
    
    # draw the shape
    glBegin(GL_LINE_LOOP)
    
    glVertex2f(x, y)
    
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    
    
    # glVertex2f(x + width, (y + height+50)/2)
    
    # glVertex2f(x + width+400, y+height+300)
    glEnd()
    
    
def draw_rotated_rect(x, y, width, height, angle):
    glPushMatrix()
    glTranslatef(x + width / 2, y + height / 2, 0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(-width / 2, -height / 2, 0)

    # set the color for the rectangle
    glColor3f(1.0, 0.0, 0.0)

    # draw the rectangle
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    glPopMatrix()

    
def draw_u_shape(**kwargs):
    x = kwargs['x']
    y = kwargs['y']
    width = kwargs['width']
    height = kwargs['height']
    space = kwargs['space']
    
    glPushMatrix()
    glTranslatef(x + width / 2, y + height / 2, 0)
    glRotatef(30, 0, 0, 1)
    glTranslatef(-width / 2, -height / 2, 0)
    # draw the shape
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x+width, y)
    glVertex2f(x+width, y+height)
    glVertex2f(x+width+space, y+height)
    glVertex2f(x+width+space, y)
    glVertex2f(x+width+space+width, y)
    glVertex2f(x+width+space+width, y)
    glVertex2f(x+width+space+width, y+height+40)
    glVertex2f(x, y+height+40)
    glVertex2f(x, y)
    
    glEnd()
    glPopMatrix()
    

    
if __name__ == "__main__":
    Logo()