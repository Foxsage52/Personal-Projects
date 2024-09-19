import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_RETURN, K_b
from classes import Warrior, Wizard, Rogue
from enemy import Goblin, Orc, Dragon
from combat_order import CombatSystem
import restore
import moves  # Import the moves module

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
CLASS_SELECTION_ITEMS = {
    'warrior': 'Warrior',
    'wizard': 'Wizard',
    'rogue': 'Rogue'
}
ENEMY_SELECTION_ITEMS = {
    'goblin': 'Goblin',
    'orc': 'Orc',
    'dragon': 'Dragon'
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

def draw_class_selection(selected_class):
    window.fill(BACKGROUND_COLOR)
    y_offset = 20
    for item, label in CLASS_SELECTION_ITEMS.items():
        color = HIGHLIGHT_COLOR if selected_class == item else TEXT_COLOR
        draw_text(label, font, color, window, 20, y_offset)
        y_offset += FONT_SIZE * 2
    draw_text("Press 'Enter' to select class, 'B' to go back", font, TEXT_COLOR, window, 20, WINDOW_HEIGHT - 40)
    pygame.display.update()

def draw_enemy_selection(selected_enemy):
    window.fill(BACKGROUND_COLOR)
    y_offset = 20
    for item, label in ENEMY_SELECTION_ITEMS.items():
        color = HIGHLIGHT_COLOR if selected_enemy == item else TEXT_COLOR
        draw_text(label, font, color, window, 20, y_offset)
        y_offset += FONT_SIZE * 2
    draw_text("Press 'Enter' to select enemy, 'B' to go back", font, TEXT_COLOR, window, 20, WINDOW_HEIGHT - 40)
    pygame.display.update()

def draw_battle_screen(character, enemy, move_list, selected_move_index):
    window.fill(BACKGROUND_COLOR)
    draw_text(f"Selected Character: {character.__class__.__name__}", font, TEXT_COLOR, window, 20, 20)
    draw_text(f"Enemy: {enemy.name}", font, TEXT_COLOR, window, 20, 60)
    
    y_offset = 100
    for i, move in enumerate(move_list):
        color = HIGHLIGHT_COLOR if i == selected_move_index else TEXT_COLOR
        draw_text(move, font, color, window, 20, y_offset)
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
    
    headers = {
        "name": "Name",
        "level": "Level",
        "hp": "Health",
        "attack": "Attack",
        "defense": "Defense",
        "mana": "Mana",
        "speed": "Speed"
    }
    
    for key, header in headers.items():
        draw_text(header, font, TEXT_COLOR, window, column_positions[key], y_offset)
    
    y_offset += FONT_SIZE * 2
    
    warrior = Warrior(level=1)
    wizard = Wizard(level=1)
    rogue = Rogue(level=1)
    
    characters = [warrior, wizard, rogue]
    
    for character in characters:
        draw_text(character.__class__.__name__, font, TEXT_COLOR, window, column_positions["name"], y_offset)
        draw_text(f"{character.level:.2f}", font, TEXT_COLOR, window, column_positions["level"], y_offset)
        draw_text(f"{character.healthpoint:.2f}", font, TEXT_COLOR, window, column_positions["hp"], y_offset)
        draw_text(f"{character.attack:.2f}", font, TEXT_COLOR, window, column_positions["attack"], y_offset)
        draw_text(f"{character.defense:.2f}", font, TEXT_COLOR, window, column_positions["defense"], y_offset)
        draw_text(f"{character.mana:.2f}", font, TEXT_COLOR, window, column_positions["mana"], y_offset)
        draw_text(f"{character.speed:.2f}", font, TEXT_COLOR, window, column_positions["speed"], y_offset)
        y_offset += FONT_SIZE * 2
    
    draw_text("Press 'B' to go back", font, TEXT_COLOR, window, 20, WINDOW_HEIGHT - 40)
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    in_game = False
    show_character_page = False
    show_class_selection = False
    show_enemy_selection = False
    show_battle_screen = False
    selected_item = 'start_game'
    selected_class = 'warrior'
    selected_enemy = 'goblin'
    character = None
    enemy = None
    move_list = []
    selected_move_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_x, mouse_y = event.pos
                    if not in_game and not show_character_page and not show_class_selection and not show_enemy_selection and not show_battle_screen:
                        y_offset = 20
                        for item in MENU_ITEMS.keys():
                            text_rect = draw_text(MENU_ITEMS[item], font, TEXT_COLOR, window, 20, y_offset)
                            if text_rect.collidepoint(mouse_x, mouse_y):
                                if item == 'start_game':
                                    show_class_selection = True
                                    show_character_page = False
                                    show_enemy_selection = False
                                    show_battle_screen = False
                                    in_game = False
                                elif item == 'view_character':
                                    show_character_page = True
                                    show_class_selection = False
                                    show_enemy_selection = False
                                    show_battle_screen = False
                                    in_game = False
                                elif item == 'quit':
                                    pygame.quit()
                                    sys.exit()
                            y_offset += FONT_SIZE * 2
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if show_class_selection:
                        if selected_class:
                            if selected_class == 'warrior':
                                character = Warrior(level=1)
                                moves.update_warrior_moves(character)  # Call the move update function for warrior
                            elif selected_class == 'wizard':
                                character = Wizard(level=1)
                                moves.update_wizard_moves(character)  # Call the move update function for wizard
                            elif selected_class == 'rogue':
                                character = Rogue(level=1)
                                moves.update_rogue_moves(character)  # Call the move update function for rogue

                            # Get the character's move list for battle
                            move_list = list(character.moves.keys())
                            show_enemy_selection = True
                            show_class_selection = False
                    elif show_enemy_selection:
                        if selected_enemy:
                            if selected_enemy == 'goblin':
                                enemy = Goblin(player=character)
                            elif selected_enemy == 'orc':
                                enemy = Orc(player=character)
                            elif selected_enemy == 'dragon':
                                enemy = Dragon(player=character)
                            
                            # Get the character's move list for battle
                            move_list = list(character.moves.keys())
                            show_battle_screen = True
                            show_enemy_selection = False
                    elif show_battle_screen:
                        pass  # Handle move selection
                    elif show_character_page:
                        show_character_page = False
                elif event.key == K_UP:
                    if show_class_selection:
                        selected_class = list(CLASS_SELECTION_ITEMS.keys())[(list(CLASS_SELECTION_ITEMS.keys()).index(selected_class) - 1) % len(CLASS_SELECTION_ITEMS)]
                    elif show_enemy_selection:
                        selected_enemy = list(ENEMY_SELECTION_ITEMS.keys())[(list(ENEMY_SELECTION_ITEMS.keys()).index(selected_enemy) - 1) % len(ENEMY_SELECTION_ITEMS)]
                    elif show_battle_screen:
                        selected_move_index = (selected_move_index - 1) % len(move_list)
                elif event.key == K_DOWN:
                    if show_class_selection:
                        selected_class = list(CLASS_SELECTION_ITEMS.keys())[(list(CLASS_SELECTION_ITEMS.keys()).index(selected_class) + 1) % len(CLASS_SELECTION_ITEMS)]
                    elif show_enemy_selection:
                        selected_enemy = list(ENEMY_SELECTION_ITEMS.keys())[(list(ENEMY_SELECTION_ITEMS.keys()).index(selected_enemy) + 1) % len(ENEMY_SELECTION_ITEMS)]
                    elif show_battle_screen:
                        selected_move_index = (selected_move_index + 1) % len(move_list)
                elif event.key == K_b:
                    if show_class_selection:
                        show_class_selection = False
                    elif show_enemy_selection:
                        show_enemy_selection = False
                    elif show_battle_screen:
                        show_battle_screen = False
                        show_class_selection = True
                    elif show_character_page:
                        show_character_page = False
                        in_game = False
                else:
                    # Handle other keys or inputs
                    pass

        if not in_game and not show_character_page and not show_class_selection and not show_enemy_selection and not show_battle_screen:
            draw_start_menu(selected_item)
        elif show_class_selection:
            draw_class_selection(selected_class)
        elif show_enemy_selection:
            draw_enemy_selection(selected_enemy)
        elif show_battle_screen:
            draw_battle_screen(character, enemy, move_list, selected_move_index)
        elif show_character_page:
            draw_character_page()

        clock.tick(30)

if __name__ == '__main__':
    main()
