#Step one creating classes
class Character:
    def __init__(self, level, healthpoint, experience, attack, defense, dex, mana, speed):
        self.level = level         # Class level
        self.healthpoint = healthpoint  # Hit points
        self.experience = experience    # Level progress
        self.attack = attack       # Attack Power
        self.defense = defense     # Defensive prowess
        self.dex = dex             # Dodge capability
        self.mana = mana           # Special meter
        self.speed = speed         # Turn order
    
    def gain_experience(self, amount):
        self.gain_experience += amount
        while self.experience >= self.level_up_requirement():
            self.level_up()
    
    def level_up_requirement():
        #Example Threshold; can be adjusted 


class Warrior(Character):
    pass

class Wizard(Character):
    pass

class Rogue(Character):
    pass

class Archer(Character):
    pass
