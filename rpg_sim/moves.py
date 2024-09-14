# Base moves for Warrior
warrior_moves = {
    "Slash": {"type": "basic", "power": 10},
    "Power Slash": {"type": "special", "power": 20},
}

# Function to update Warrior moves
def update_warrior_moves(character):
    if isinstance(character, Warrior):
        if character.level >= 5:
            character.moves["Shield Bash"] = {"type": "basic", "power": 15}
            character.moves["War Cry"] = {"type": "special", "power": 0, "effect": "attack up"}
            print("Warrior learned Shield Bash and War Cry!")
        if character.level >= 10:
            character.moves["Cleave"] = {"type": "special", "power": 25}
            character.moves["Rally"] = {"type": "buff", "power": 0, "effect": "defense up"}
            print("Warrior learned Cleave and Rally!")

# Base moves for Wizard
wizard_moves = {
    "Fireball": {"type": "special", "power": 30},
    "Lightning Bolt": {"type": "special", "power": 25},
}

# Function to update Wizard moves
def update_wizard_moves(character):
    if isinstance(character, Wizard):
        if character.level >= 5:
            character.moves["Frostbolt"] = {"type": "special", "power": 20}
            character.moves["Mana Shield"] = {"type": "buff", "power": 0, "effect": "reduce damage"}
            print("Wizard learned Frostbolt and Mana Shield!")
        if character.level >= 10:
            character.moves["Meteor"] = {"type": "special", "power": 40}
            character.moves["Arcane Intellect"] = {"type": "buff", "power": 0, "effect": "increase mana"}
            print("Wizard learned Meteor and Arcane Intellect!")

# Add similar logic for Rogue and Archer
