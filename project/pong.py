import pygame
import random
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Set up the game window
window_width = 800
window_height = 700
window = pygame.display.set_mode((window_width, window_height), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Welcome to Pong!")

# Load and play background music
pong_sound = pygame.mixer.Sound("pong.wav")

background_music_path = "bg.mp3"  # Ensure this path is correct
pygame.mixer.music.load(background_music_path)

pygame.mixer.music.play(-1)  # Play music indefinitely

# OpenGL setup
def setup_opengl():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, window_width, window_height, 0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

setup_opengl()

# Set up fonts
# Assuming the font file is named 'Orbitron-Regular.ttf' and is located in the project folder
font_path = "Orbitron-Regular.ttf"
font_size = 32
font = pygame.font.Font(font_path, font_size)

# Global variables
ball_speed = 0.85
paddle_speed = 0.95
ball_size = 10
paddle_height = 400

paddle_width = 10
paddle1_x = 20
paddle1_y = window_height // 2 - paddle_height // 2
paddle2_x = window_width - 20 - paddle_width
paddle2_y = window_height // 2 - paddle_height // 2

ball_speed_x = ball_speed
ball_speed_y = ball_speed
ball_x = window_width // 2 - ball_size // 2
ball_y = window_height // 2 - ball_size // 2

score1 = 0
score2 = 0
game_over = False
running = True

# Function to draw text
def draw_text(text, x, y, font_size=None, color=(255, 255, 255)):
    if font_size is None:
        font_size = 32  # Default font size or use a global variable if defined
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

# Function to draw a rectangle
def draw_rect(x, y, width, height, color):
    glColor3fv(color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Function to handle paddle movement
def move_paddles(keys, paddle1_y, paddle2_y):
    global paddle_speed
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
        paddle2_y += paddle_speed
    return paddle1_y, paddle2_y

# Function to move the ball and check collisions
def move_ball(ball_x, ball_y, ball_speed_x, ball_speed_y, paddle1_x, paddle1_y, paddle2_x, paddle2_y):
    global paddle_height, paddle_width
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    

    # Check for ball collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
        pong_sound.play()
    if ball_x >= paddle2_x - ball_size and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)
        pong_sound.play()

    # Check for ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_size:
        ball_speed_y = -ball_speed_y

    return ball_x, ball_y, ball_speed_x, ball_speed_y

# Function to check if the ball is out of bounds and update the score
def check_out_of_bounds(ball_x, ball_y, ball_speed_x, ball_speed_y, score1, score2):
    global ball_speed
    if ball_x <= 0:
        score2 += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_speed_x = random.choice([-ball_speed, ball_speed])
        ball_speed_y = random.choice([-ball_speed, ball_speed])
    if ball_x >= window_width - ball_size:
        score1 += 1
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_speed_x = random.choice([-ball_speed, ball_speed])
        ball_speed_y = random.choice([-ball_speed, ball_speed])
    return ball_x, ball_y, ball_speed_x, ball_speed_y, score1, score2

# Function to draw the score
def draw_score(score1, score2):
    score_text = font.render(str(score1) + " - " + str(score2), True, (255, 255, 255))
    text_surface = pygame.image.tostring(score_text, 'RGBA', True)
    glRasterPos2d(window_width // 2 - score_text.get_width() // 2, 50)
    glDrawPixels(score_text.get_width(), score_text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_surface)

# Function to display game over screen
def display_game_over():
    global game_over, score1, score2, running
    glClear(GL_COLOR_BUFFER_BIT)
    if score1 > score2:
        winner_text = "Player 1 wins!"
    elif score2 > score1:
        winner_text = "Player 2 wins!"
    else:
        winner_text = "It's a tie!"
    draw_text(winner_text, window_width // 2 - 100, window_height // 2 - 20)
    draw_text("Press 'R' to retry or 'M' to go to menu", window_width // 2 - 325, window_height // 2 + 30)
    pygame.display.flip()
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score1 = 0
                    score2 = 0
                    game_over = False
                if event.key == pygame.K_m:
                    game_over = False
                    menu_screen()

def settings_screen():
    global paddle_height, ball_speed, ball_size
    settings_running = True
    while settings_running:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("Welcome to the Settings Page!", window_width // 2 - 280, window_height // 2 - 250)
        draw_text(f">Paddle Height: {paddle_height}", window_width // 2 - 150, window_height // 2 - 150)
        draw_text(f">Ball Speed: {ball_speed}", window_width // 2 - 150, window_height // 2 - 40)
        draw_text(f">Ball Size: {ball_size}", window_width // 2 - 150, window_height // 2 + 50)
        draw_text(f"W/S-Paddle Height", window_width // 2 - 400, window_height // 2 + 150,  16)
        draw_text(f"A/D-BallSpeed", window_width // 2 - 100, window_height // 2 + 150,  16)
        draw_text(f"Z/X-Ball Size", window_width // 2 + 200, window_height // 2 + 150,  16)
        draw_text("Press 'B' to go Back", window_width // 2 - 180, window_height // 2 + 240)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
                settings_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    settings_running = False
                elif event.key == pygame.K_w:
                    paddle_height += 10
                elif event.key == pygame.K_s:
                    paddle_height = max(10, paddle_height - 10)
                elif event.key == pygame.K_a:
                    ball_speed += 0.1
                elif event.key == pygame.K_d:
                    ball_speed = max(0.1, ball_speed - 0.1)
                elif event.key == pygame.K_z:
                    ball_size += 1
                elif event.key == pygame.K_x:
                    ball_size = max(1, ball_size - 1)

def menu_screen():
    global running, game_over
    menu_running = True
    while menu_running:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("Welcome to Pong!", window_width // 2 - 150, window_height // 2 - 20)
        draw_text("Press 'P' to Play, 'Q' to Quit, 'S' for Settings", window_width // 2 - 368, window_height // 2 + 50)
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_over = False
                    menu_running = False
                elif event.key == pygame.K_q:
                    running = False
                    menu_running = False
                elif event.key == pygame.K_s:
                    settings_screen()

# Main game loop
def game_loop():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle1_y, paddle2_y, score1, score2, game_over, running
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the paddles
        keys = pygame.key.get_pressed()
        paddle1_y, paddle2_y = move_paddles(keys, paddle1_y, paddle2_y)

        # Move the ball
        ball_x, ball_y, ball_speed_x, ball_speed_y = move_ball(ball_x, ball_y, ball_speed_x, ball_speed_y, paddle1_x, paddle1_y, paddle2_x, paddle2_y)

        # Check for ball going out of bounds
        ball_x, ball_y, ball_speed_x, ball_speed_y, score1, score2 = check_out_of_bounds(ball_x, ball_y, ball_speed_x, ball_speed_y, score1, score2)

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the paddles
        draw_rect(paddle1_x, paddle1_y, paddle_width, paddle_height, (255, 255, 255))
        draw_rect(paddle2_x, paddle2_y, paddle_width, paddle_height, (255, 255, 255))

        # Draw the ball
        draw_rect(ball_x, ball_y, ball_size, ball_size, (255, 255, 255))

        # Draw the score
        draw_score(score1, score2)

        # Update the display
        pygame.display.flip()

        # Check for game over
        if score1 == 5 or score2 == 5:
            game_over = True

        # Game over screen
        if game_over:
            display_game_over()

# Start the game loop
menu_screen()
game_loop()

# Quit the game
pygame.quit()
