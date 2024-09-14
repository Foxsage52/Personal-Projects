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
        self.experience += amount
        while self.experience >= self.level_up_requirement():
            self.level_up()
    
    def level_up_requirement(self):
        #Example Threshold; can be adjusted
        return 50 * self.level
    
    def level_up(self):
        self.experience -= self.level_up_requirement()
        self.level +=1
        return f"Congratulations! {self.level} reached!"
    
    def __str__(self):
        return (f"{self.__class__.__name__}(Level: {self.level}, Health: {self.healthpoint}, "
                f"Attack: {self.attack}, Defense: {self.defense}, Dexterity: {self.dex}, "
                f"Mana: {self.mana}, Speed: {self.speed})")



class Warrior(Character):
    pass

class Wizard(Character):
    pass

class Rogue(Character):
    pass

class Archer(Character):
    pass

