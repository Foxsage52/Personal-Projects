from classes import Warrior, Wizard, Rogue
from combat_order import Combat
from enemy import Goblin, Orc, Dragon

# Create character and enemy instances
warrior = Warrior(level=10)
wizard = Wizard(level=10)
rogue = Rogue(level=10)

goblin = Goblin(player=warrior)   # Enemy instance for the warrior to fight
orc = Orc(player=wizard)         # Enemy instance for the wizard to fight
dragon = Dragon(player=rogue)    # Enemy instance for the rogue to fight

# Example combat scenarios
combat_warrior_goblin = Combat(attacker=warrior, defender=goblin)
print(combat_warrior_goblin.take_turn("Power Slash"))

combat_wizard_orc = Combat(attacker=wizard, defender=orc)
print(combat_wizard_orc.take_turn("Ignite"))

combat_rogue_dragon = Combat(attacker=rogue, defender=dragon)
print(combat_rogue_dragon.take_turn("Back Stab"))
