# import the pygame library and initialize the game engine
import pygame
pygame.init()

# import custom classes
from paddle import Paddle

# define some colors
ORANGE = (255, 153, 0)
WHITE = (255, 255, 255)

# create a game window
window_size = (500, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

# create paddles
paddleA = Paddle(WHITE, 100, 10, 200, 0)
paddleB = Paddle(WHITE, 100, 10, 200, 690)

# create sprite group and add sprites to group
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# flag to determine if game is ongoing
continue_game = True

# clock is used to control how fast the screen updates
clock = pygame.time.Clock()

# ---------- Main Program Loop ------------
while continue_game:
    # --- Main event loop
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT:  # user clicked close
            continue_game = False  # flag to discontinue game

    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        paddleA.moveLeft(5)
    if keys[pygame.K_s]:
        paddleA.moveRight(5)
    if keys[pygame.K_RIGHT]:
        paddleB.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddleB.moveLeft(5)    

    # --- game logic will go here
    all_sprites_list.update()

    # --- Drawing code goes here
    screen.fill(ORANGE)  # set screen to orange
    pygame.draw.line(screen, WHITE, [0, 350], [500, 350], 5)
    all_sprites_list.draw(screen)

    # --- update display with what was drawn
    pygame.display.flip()

    # --- Set frame rate to 60 frames per second
    clock.tick(60)

# Exit game
pygame.quit()
