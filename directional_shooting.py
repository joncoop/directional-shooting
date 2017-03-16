# Imports
import pygame
import math

# Initialize game engine
pygame.init()

# Window
TITLE = "Pew! Pew! Pew!"
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game classes
class Gun:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        loc = round(self.x), round(self.y) 
        pygame.draw.circle(surface, WHITE, loc, 10)
        
class Bullet:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        loc = round(self.x), round(self.y)
        pygame.draw.circle(surface, RED, loc, 10)


# Game objects
gun =  Gun(400, 300)
bullets = []

# Game settings
speed = 5

# Helper functions
def get_velocity_vector(x1, y1, x2, y2, speed):
    #return x2 - x1, y2 - y1
    #return (x2 - x1) / 10, (y2 - y1) / 10
    
    a = x2 - x1
    b = y2 - y1

    if a == 0 and b == 0:
        return 0, 0
    
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
            x1, y1 = gun.x, gun.y
            x2, y2 = pygame.mouse.get_pos()
            
            vx, vy = get_velocity_vector(x1, y1, x2, y2, speed)

            if vx != 0 or vy != 0:
                b = Bullet(x1, y1, vx, vy)
                bullets.append(b)
            else:
                print("You clicked the exact middle. No shot fired.")

    # Game logic
    to_remove = []
    
    for b in bullets:
        b.update()

        if b.x < 0 or b.x > WIDTH or b.y < 0 or b.y > HEIGHT:
            to_remove.append(b)

    for b in to_remove:
        bullets.remove(b)

    # Drawing code
    window.fill(BLACK)
    
    gun.draw(window)
    
    for b in bullets:
        b.draw(window)
        
    # Update screen
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
