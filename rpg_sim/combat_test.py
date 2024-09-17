from classes import Warrior, Wizard
from combat_framework import Combat

# Create character instances
warrior = Warrior(level=5)
wizard = Wizard(level=5)

# Set up combat
combat = Combat(attacker=warrior, defender=wizard)


# Special Move usage
# Warrior attacks with "Power Slash"
print(combat.attack("Power Slash"))

# Wizard uses "Ignite"
combat.attacker = wizard
print(combat.attack("Ignite"))

#Setting up basic attack usage
# Warrior attacks with "Slash"
combat.attacker = warrior
print(combat.attack("Slash"))

# Wizard uses "Force"
combat.attacker = wizard
print(combat.attack("Flare"))