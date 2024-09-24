# moves.py

import classes  # No need to import individual classes as update functions are already class-specific.
from blocking import Block  # Import Block to add it to universal moves

# Universal Moves
universal_moves = {
    "Block": Block.block_move(),  # Add Block move to universal moves
}

# Base moves for Warrior
warrior_moves = {
    "Slash": {"type": "basic", "power": 15, "regen": 5},
    "Power Slash": {"type": "special", "power": 20, "cost": 5},
    "Invigorating Shout": {"type": "special", "power": 0, "heal_percent": 50, "cost": 0}  # Restores 50% health and mana
}

# Function to update Warrior moves
def update_warrior_moves(character):
    if isinstance(character, classes.Warrior):
        character.moves.update(universal_moves)  # Add universal moves
        if character.level >= 5:
            character.moves["Shield Bash"] = {"type": "basic", "power": 10, "regen": 4}
            character.moves["War Cry"] = {"type": "special", "power": 15, "cost": 2}
            print("Warrior learned Shield Bash and War Cry!")
        if character.level >= 10:
            character.moves["Power Cleave"] = {"type": "special", "power": 25, "cost": 5 }
            character.moves["Stab"] = {"type": "basic", "power": 20, "regen": 5}
            print("Warrior learned Cleave and Stab!")

# Base moves for Wizard
wizard_moves = {
    "Force": {"type": "basic", "power": 15, "regen": 2},
    "Ignite": {"type": "special", "power": 15, "cost": 3},  # Added default cost
    "Restore Body": {"type": "special", "power": 0, "heal_percent": 50, "cost": 0}  # Restores 50% health and mana
}

# Function to update Wizard moves
def update_wizard_moves(character):
    if isinstance(character, classes.Wizard):
        character.moves.update(universal_moves)  # Add universal moves
        if character.level >= 5:
            character.moves["Flare"] = {"type": "basic", "power": 20, "regen": 4}
            character.moves["Magic Bolt"] = {"type": "special", "power": 25, "cost": 8}
            print("Wizard learned Flare and Magic Bolt!")
        if character.level >= 10:
            character.moves["Fireball"] = {"type": "special", "power": 30, "cost": 10}
            character.moves["Smite"] = {"type": "basic", "power": 20, "regen": 5}
            print("Wizard learned Fireball and Smite!")

# Base moves for Rogue
rogue_moves = {
    "Dagger Strike": {"type": "basic", "power": 15, "regen": 2},
    "Back Stab": {"type": "special", "power": 20, "cost": 3},  # Added default cost
    "Blood Bath": {"type": "special", "power": 0, "heal_percent": 50, "cost": 0}  # Restores 50% health and mana
}

# Function to update Rogue moves
def update_rogue_moves(character):
    if isinstance(character, classes.Rogue):
        character.moves.update(universal_moves)  # Add universal moves
        if character.level >= 5:
            character.moves["Barrage Strike"] = {"type": "basic", "power": 20, "regen": 3}
            character.moves["Shadow Strike"] = {"type": "special", "power": 15, "cost": 5}
            print("Rogue learned Barrage Strike and Shadow Strike!")
        if character.level >= 10:
            character.moves["Shadow Palm"] = {"type": "special", "power": 25, "cost": 7}  # Added default cost
            character.moves["Plunge"] = {"type": "basic", "power": 20, "regen": 4}
            print("Rogue learned Shadow Palm and Plunge!")