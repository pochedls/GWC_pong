# import the pygame library and initialize the game engine
import pygame
pygame.init()

# define some colors
ORANGE = (255, 153, 0)
WHITE = (255, 255, 255)

# create a game window
window_size = (500, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

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

    # --- game logic will go here

    # --- Drawing code goes here
    screen.fill(ORANGE)  # set screen to orange
    pygame.draw.line(screen, WHITE, [0, 350], [500, 350], 5)

    # --- update display with what was drawn
    pygame.display.flip()

    # --- Set frame rate to 60 frames per second
    clock.tick(60)

# Exit game
pygame.quit()
