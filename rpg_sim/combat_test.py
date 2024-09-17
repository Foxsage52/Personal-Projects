from classes import Warrior, Wizard
from combat_framework import Combat

# Create character instances
warrior = Warrior(level=5)
wizard = Wizard(level=5)

# Set up combat: Warrior attacks Wizard
combat = Combat(attacker=warrior, defender=wizard)

# Warrior attacks with "Power Slash" (special move)
print(combat.attack("Power Slash"))

# Warrior attacks with "Slash" (basic move)
print(combat.attack("Slash"))

# Set up combat: Wizard attacks Warrior
combat2 = Combat(attacker=wizard, defender=warrior)

# Wizard attacks with "Ignite" (special move)
print(combat2.attack("Ignite"))

# Wizard attacks with "Force" (basic move)
print(combat2.attack("Force"))
