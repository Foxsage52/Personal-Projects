import classes
# Universal Moves
universal_moves = {
    "Heal": {"type": "special", "power": 0, "heal": 20, "cost": 3},
    "Block": {"type": "basic", "power": 0, "block": True},
}

# Base moves for Warrior
warrior_moves = {
    "Slash": {"type": "basic", "power": 10, "regen": 1},
    "Power Slash": {"type": "special", "power": 20, "cost": 2},
}

# Function to update Warrior moves
def update_warrior_moves(character):
    if isinstance(character, classes.Warrior):
        if character.level >= 5:
            character.moves["Shield Bash"] = {"type": "basic", "power": 15, "regen": 1}
            character.moves["War Cry"] = {"type": "special", "power": 10, "cost": 2}
            print("Warrior learned Shield Bash and War Cry!")
        if character.level >= 10:
            character.moves["Cleave"] = {"type": "special", "power": 25, "cost": 2 }
            character.moves["Stab"] = {"type": "basic", "power": 15, "regen": 1}
            print("Warrior learned Cleave and Stab!")
            
wizard_moves = {
    "Force": {"type": "basic", "power": 10, "regen": 1},
    "Ignite": {"type": "special", "power": 20},
}

# # Function to update wizard moves
def update_wizard_moves(character):
    if isinstance(character, classes.Wizard):
        if character.level >= 5:
            character.moves["Flare"] = {"type": "basic", "power": 15, "regen": 1}
            character.moves["Magic Bolt"] = {"type": "special", "power": 10, "cost": 2}
            print("Wizard learned Flare and Magic Bolt!")
        if character.level >= 10:
            character.moves["Fireball"] = {"type": "special", "power": 25}
            character.moves["Smite"] = {"type": "basic", "power": 15, "regen": 1, "cost": 2}
            print("Wizard learned Fireball and Smite!")