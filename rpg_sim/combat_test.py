from classes import Warrior, Wizard, Rogue
from combat_order import CombatSystem
from enemy import Goblin, Orc, Dragon

# Create character and enemy instances
warrior = Warrior(level=10)
wizard = Wizard(level=10)
rogue = Rogue(level=10)

goblin = Goblin(player=warrior)   # Enemy instance for the warrior to fight
orc = Orc(player=wizard)         # Enemy instance for the wizard to fight
dragon = Dragon(player=rogue)    # Enemy instance for the rogue to fight

print(goblin)
print(orc)
print(dragon)

# Example combat scenarios
combat_warrior_goblin = CombatSystem(user=warrior, enemy=goblin)
print(combat_warrior_goblin.combat_round("Power Slash"))

combat_wizard_orc = CombatSystem(user=wizard, enemy=orc)
print(combat_wizard_orc.combat_round("Ignite"))

combat_rogue_dragon = CombatSystem(user=rogue, enemy=dragon)
print(combat_rogue_dragon.combat_round("Back Stab"))
