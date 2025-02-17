# Import the open-source pygame library
import pygame
# Import from constants database file
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the window title
    pygame.display.set_caption("Asteroids Game")

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the window is closed
                return  # Exit the game loop

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()  # Start the game
