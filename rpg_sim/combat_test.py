from classes import Warrior, Wizard, Rogue
from combat_framework import Combat
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
print(f"Warrior used 'Power Slash' on Goblin. {combat_warrior_goblin.attack('Power Slash')}")  # Warrior uses a special move on Goblin
print(f"Warrior used 'Slash' on Goblin. {combat_warrior_goblin.attack('Slash')}")        # Warrior uses a basic move on Goblin

# Goblin attacks Warrior
combat_goblin_warrior = Combat(attacker=goblin, defender=warrior)
goblin_move = goblin.choose_move()
print(f"Goblin used '{goblin_move}' on Warrior. {combat_goblin_warrior.attack(goblin_move)}")  # Goblin attacks Warrior using a random move

# Wizard vs Orc
combat_wizard_orc = Combat(attacker=wizard, defender=orc)

print("\nWizard vs Orc Combat:")
print(f"Wizard used 'Ignite' on Orc. {combat_wizard_orc.attack('Ignite')}")  # Wizard uses a special move on Orc
print(f"Wizard used 'Force' on Orc. {combat_wizard_orc.attack('Force')}")   # Wizard uses a basic move on Orc

# Orc attacks Wizard
combat_orc_wizard = Combat(attacker=orc, defender=wizard)
orc_move = orc.choose_move()
print(f"Orc used '{orc_move}' on Wizard. {combat_orc_wizard.attack(orc_move)}")  # Orc attacks Wizard using a random move

# Rogue vs Dragon
combat_rogue_dragon = Combat(attacker=rogue, defender=dragon)

print("\nRogue vs Dragon Combat:")
print(f"Rogue used 'Back Stab' on Dragon. {combat_rogue_dragon.attack('Back Stab')}")    # Rogue uses a special move on Dragon
print(f"Rogue used 'Dagger Strike' on Dragon. {combat_rogue_dragon.attack('Dagger Strike')}")  # Rogue uses a basic move on Dragon

# Dragon attacks Rogue
combat_dragon_rogue = Combat(attacker=dragon, defender=rogue)
dragon_move = dragon.choose_move()
print(f"Dragon used '{dragon_move}' on Rogue. {combat_dragon_rogue.attack(dragon_move)}")  # Dragon attacks Rogue using a random move
