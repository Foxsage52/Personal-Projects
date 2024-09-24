# Text-Based RPG Game

## Version 0.6

## Overview

This is a simple text-based RPG game built using Python and Pygame. The game features a main menu with options to start the game, view character statistics, or quit. Upon starting the game, players are prompted to select a character class from available options. The game includes functionality to display and manage character stats.

## Features

- **Main Menu**: Options to "Start Game", "View Character", and "Quit".
- **Character Class Selection**: Choose from Warrior, Wizard, and Rogue.
- **Character Stats Display**: View detailed stats of each character class, including level, health, attack, defense, mana, and speed.
- **Combat System**: Engage in battles with various enemies and progress through different levels.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install pygame
   ```

6. Run the game script:
   ```bash
   python game_start.py
   ```

## Usage

- **Main Menu**: Select an option using the mouse or keyboard.
  - Click "Start Game" to proceed to the class selection screen.
  - Click "View Character" to view the base stats of each character class.
  - Click "Quit" to exit the game.
- **Class Selection**: Choose a character class (Warrior, Wizard, Rogue) to start the game.
- **Character Stats**: View detailed stats of each character class on the character page.
- **Combat**: Engage in battles with enemies, select moves, and progress through levels.

## Key Files

- `game_start.py`: The main game script containing the core logic and user interface.
- `classes.py`: Contains definitions for character classes (Warrior, Wizard, Rogue).
- `moves.py`: Defines universal moves and their effects.
- `combat_order.py`: Manages the combat system.
- `attack.py`: Establishes attacking mechanics.
- `healing.py`: Manages healing mechanics.
- `enemy.py`: Contains the enemy classes (Goblin, Orc, Dragon).
- `system.py`: Contains system-level utilities and configurations.
- `testing.py`: A file to use to ensure that Python is working properly and for making any tweaks to the other files.

## Development

### Current Version: 0.6

### Next Steps:
- Implement additional combat mechanics.
- Develop enemy and their mechanics.
- Improve user interface and add more interactions.
- Add more enemies.
- Expand on player levels.

## Contact

For any questions or feedback, please contact:
- Email: foxsage52@gmail.com
- GitHub: [Foxsage52](https://github.com/Foxsage52)