# Imports
import pygame
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Bang!"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game objects
gun = {'x': 400, 'y': 300}
bullets = []
bullet_speed = 5

def get_velocity_vector(x1, y1, x2, y2, speed):
    #return x2 - x1, y2 - y1
    #return (x2 - x1) / 10, (y2 - y1) / 10
    
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(a**2 + b**2)

    vx = speed * a / c
    vy = speed * b / c

    return vx, vy

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = gun['x'], gun['y']
            x2, y2 = pygame.mouse.get_pos()

            vx, vy = get_velocity_vector(x1, y1, x2, y2, bullet_speed)
            
            b = {'x': x1, 'y': y1, 'vx': vx, 'vy': vy}
            bullets.append(b)

    # Game logic
    to_remove = []
    
    for b in bullets:
        b['x'] += b['vx']
        b['y'] += b['vy']

        if b['x'] < 0 or b['x'] > 800 or b['y'] < 0 or b['y'] > 600:
            to_remove.append(b)

    for b in to_remove:
        bullets.remove(b)

    # Drawing code
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (gun['x'], gun['y']), 10)

    for b in bullets:
        b_x = round(b['x'])
        b_y = round(b['y'])
        pygame.draw.circle(screen, RED, (b_x, b_y), 10)
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
