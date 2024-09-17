from classes import Warrior
from enemy import Goblin, Orc, Dragon

# Create a Warrior instance
warrior = Warrior(level=1)
warrior.gain_experience(500)

# Create enemies based on the warrior's stats
goblin = Goblin(player=warrior)
orc = Orc(player=warrior)
dragon = Dragon(player=warrior)

# Print warrior and enemy stats
print(warrior)
print(goblin)
print(orc)
print(dragon)
