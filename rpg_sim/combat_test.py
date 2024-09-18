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

# Warrior vs Goblin
combat_warrior_goblin = Combat(attacker=warrior, defender=goblin)

print("Warrior vs Goblin Combat:")
print(combat_warrior_goblin.take_turn('Power Slash'))  # Warrior uses a special move on Goblin
print(combat_warrior_goblin.take_turn('Slash'))        # Warrior uses a basic move on Goblin

# Goblin attacks Warrior
combat_goblin_warrior = Combat(attacker=goblin, defender=warrior)
goblin_move = goblin.choose_move()
print(f"Goblin used '{goblin_move}' on Warrior. {combat_goblin_warrior.take_turn(goblin_move)}")

# Wizard vs Orc
combat_wizard_orc = Combat(attacker=wizard, defender=orc)

print("\nWizard vs Orc Combat:")
print(combat_wizard_orc.take_turn('Ignite'))  # Wizard uses a special move on Orc
print(combat_wizard_orc.take_turn('Force'))   # Wizard uses a basic move on Orc

# Orc attacks Wizard
combat_orc_wizard = Combat(attacker=orc, defender=wizard)
orc_move = orc.choose_move()
print(f"Orc used '{orc_move}' on Wizard. {combat_orc_wizard.take_turn(orc_move)}")

# Rogue vs Dragon
combat_rogue_dragon = Combat(attacker=rogue, defender=dragon)

print("\nRogue vs Dragon Combat:")
print(combat_rogue_dragon.take_turn('Back Stab'))    # Rogue uses a special move on Dragon
print(combat_rogue_dragon.take_turn('Dagger Strike'))  # Rogue uses a basic move on Dragon

# Dragon attacks Rogue
combat_dragon_rogue = Combat(attacker=dragon, defender=rogue)
dragon_move = dragon.choose_move()
print(f"Dragon used '{dragon_move}' on Rogue. {combat_dragon_rogue.take_turn(dragon_move)}")
