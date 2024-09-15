import pygame
import sys
from pygame.locals import *
from classes import Warrior  # Ensure this import matches your file structure
import moves

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 24
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Text-Based RPG')

# Set up the font
font = pygame.font.Font(None, FONT_SIZE)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    clock = pygame.time.Clock()
    warrior = Warrior()  # Create a Warrior object

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:  # Press 'Q' to quit
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:  # Gain experience on space bar press
                    warrior.gain_experience(500)

        # Fill the background
        window.fill(BACKGROUND_COLOR)

        # Draw Warrior's stats and moves
        stats_text = str(warrior)
        moves_text = "Moves:\n" + warrior.format_moves()
        text_lines = stats_text.split('\n') + moves_text.split('\n')
        
        y_offset = 20
        for line in text_lines:
            draw_text(line, font, TEXT_COLOR, window, 20, y_offset)
            y_offset += FONT_SIZE

        # Update the display
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
