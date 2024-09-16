import pygame
import sys
from pygame.locals import *
from classes import Warrior, Wizard, Rogue, Archer  # Import character classes

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 24
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 0, 0)  # Color for highlighted text
MENU_ITEMS = {
    'start_game': 'Start Game',
    'view_character': 'View Character',
    'quit': 'Quit'
}

# Initialize Pygame
pygame.init()

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
    return textrect

def draw_start_menu(selected_item):
    window.fill(BACKGROUND_COLOR)
    y_offset = 20
    for item, label in MENU_ITEMS.items():
        color = HIGHLIGHT_COLOR if selected_item == item else TEXT_COLOR
        draw_text(label, font, color, window, 20, y_offset)
        y_offset += FONT_SIZE * 2
    pygame.display.update()

def draw_character_page():
    window.fill(BACKGROUND_COLOR)
    y_offset = 20
    column_positions = {
        "name": 20,
        "level": 150,
        "hp": 250,
        "attack": 350,
        "defense": 450,
        "mana": 550,
        "speed": 650
    }
    
    # Create instances of each character class
    warrior = Warrior()
    wizard = Wizard()
    rogue = Rogue()
    archer = Archer()
    
    characters = [warrior, wizard, rogue, archer]
    
    # Display the character names and stats in separate columns
    for character in characters:
        draw_text(character.__class__.__name__, font, TEXT_COLOR, window, column_positions["name"], y_offset)
        draw_text(str(character.level), font, TEXT_COLOR, window, column_positions["level"], y_offset)
        draw_text(str(character.healthpoint), font, TEXT_COLOR, window, column_positions["hp"], y_offset)
        draw_text(str(character.attack), font, TEXT_COLOR, window, column_positions["attack"], y_offset)
        draw_text(str(character.defense), font, TEXT_COLOR, window, column_positions["defense"], y_offset)
        draw_text(str(character.mana), font, TEXT_COLOR, window, column_positions["mana"], y_offset)
        draw_text(str(character.speed), font, TEXT_COLOR, window, column_positions["speed"], y_offset)
        y_offset += FONT_SIZE * 2
    
    # Draw back button
    draw_text("Press 'B' to go back", font, TEXT_COLOR, window, 20, WINDOW_HEIGHT - 40)
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    in_game = False
    show_character_page = False
    selected_item = 'start_game'

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_x, mouse_y = event.pos
                    if not in_game and not show_character_page:
                        y_offset = 20
                        for item in MENU_ITEMS.keys():
                            text_rect = draw_text(MENU_ITEMS[item], font, TEXT_COLOR, window, 20, y_offset)
                            if text_rect.collidepoint(mouse_x, mouse_y):
                                if item == 'start_game':
                                    in_game = True
                                    show_character_page = False  # Reset state
                                elif item == 'view_character':
                                    show_character_page = True
                                    in_game = False  # Ensure you're not in the game state
                                elif item == 'quit':
                                    pygame.quit()
                                    sys.exit()
                            y_offset += FONT_SIZE * 2
                    elif show_character_page:
                        back_button_rect = draw_text("Press 'B' to go back", font, TEXT_COLOR, window, 20, WINDOW_HEIGHT - 40)
                        if back_button_rect.collidepoint(mouse_x, mouse_y):
                            show_character_page = False
                            in_game = False
            elif event.type == KEYDOWN:
                if event.key == K_b and show_character_page:  # Press 'B' to go back
                    show_character_page = False
                elif event.key == K_SPACE and in_game:  # Placeholder action for Start Game
                    pass  # Currently does nothing

        if not in_game and not show_character_page:
            draw_start_menu(selected_item)
        elif show_character_page:
            draw_character_page()
        else:
            window.fill(BACKGROUND_COLOR)
            draw_text("Game Started", font, TEXT_COLOR, window, 20, 20)
            pygame.display.update()

        clock.tick(30)

if __name__ == "__main__":
    main()
