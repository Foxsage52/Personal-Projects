from classes import Warrior, Wizard
from combat_framework import Combat

# Create character instances
warrior = Warrior(level=10)
wizard = Wizard(level=10)

# Set up combat
combat = Combat(attacker=warrior, defender=wizard)

# Warrior attacks with "Power Slash"
print(combat.attack("Power Slash"))

# Wizard uses "Ignite"
combat.attacker = wizard
print(combat.attack("Ignite"))
