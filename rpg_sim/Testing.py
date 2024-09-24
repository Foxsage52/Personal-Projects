from classes import Wizard
from enemy import Goblin, Orc, Dragon
from combat_order import CombatSystem

# Create a Wizard instance
wizard = Wizard()

# Store initial health and mana
initial_health = wizard.health
initial_mana = wizard.mana

# Create enemy instances
goblin = Goblin(player=wizard)
orc = Orc(player=wizard)
dragon = Dragon(player=wizard)

print(wizard)
print(goblin)

# Function to display available moves
def display_moves():
    print("Available moves:")
    for move in wizard.moves.keys():
        print(f"- {move}")

# Function to handle combat
def combat_scenario(enemy):
    combat = CombatSystem(user=wizard, enemy=enemy)
    while wizard.health > 0 and enemy.health > 0:
        display_moves()
        player_move = input("Choose your move: ")
        if player_move not in wizard.moves:
            print("Invalid move. Please choose again.")
            continue

        # Execute player's move
        print(combat.combat_round(player_move))

        # Check if the enemy is defeated
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            return True

        # Check if the wizard is defeated
        if wizard.health <= 0:
            print(f"{wizard.__class__.__name__} has been defeated!")
            return False

# Combat sequence
if combat_scenario(goblin):
    wizard.level = 10
    wizard.health = initial_health  # Reset health
    wizard.mana = initial_mana  # Reset mana
    print(f"{wizard.__class__.__name__} leveled up to 10!")
    if combat_scenario(orc):
        wizard.level = 15
        wizard.health = initial_health  # Reset health
        wizard.mana = initial_mana  # Reset mana
        print(f"{wizard.__class__.__name__} leveled up to 15!")
        if combat_scenario(dragon):
            wizard.level = 20
            wizard.health = initial_health  # Reset health
            wizard.mana = initial_mana  # Reset mana
            print(f"{wizard.__class__.__name__} leveled up to 20!")
            print("Congratulations! You have defeated all enemies.")