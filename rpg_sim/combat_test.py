from classes import Warrior, Wizard, Rogue
from combat_framework import Combat

# Create character instances
warrior = Warrior(level=10)
wizard = Wizard(level=10)
rogue = Rogue(level=10)

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

# Set up combat: Rogue attacks Warrior
combat3 = Combat(attacker=rogue, defender=warrior)

# Rogue attacks with "Back Stab" (special move)
print(combat3.attack("Back Stab"))

# Rogue attacks with "Dagger Strike" (basic move)
print(combat3.attack("Dagger Strike"))
