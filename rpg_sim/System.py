#Step one creating The system
class System:
    def __init__(self, level, healthpoint, experience, attack, defense, m_defense, mana, speed):
        self.level = level         # Class level
        self.healthpoint = healthpoint  # Hit points
        self.experience = experience    # Level progress
        self.attack = attack       # Attack Power
        self.defense = defense     # Defensive prowess
        self.m_defense = m_defense             # Dodge capability
        self.mana = mana           # Special Attack
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
        return (f"{self.__class__.__name__}\n"
                f"Level: {self.level}\n"
                f"Experience: {self.experience}/{self.level_up_requirement()}\n"
                f"Health: {self.healthpoint}\n"
                f"Attack: {self.attack}\n"
                f"Defense: {self.defense}\n" 
                f"M. Defense: {self.m_defense}\n"
                f"Mana: {self.mana}\n"
                f"Speed: {self.speed}\n")



class Warrior(System):
    def __init__(self, level = 1, experience = 0, healthpoint=100, attack=20, defense=15, m_defense=10, mana=5, speed=10):
        super().__init__(level, healthpoint, experience, attack, defense, m_defense, mana, speed)
    def level_up(self):
        super().level_up()
        self.healthpoint += 15
        self.attack += 10
        self.defense += 5
        self.m_defense +=3
        self.mana += 4
        self.speed += 5
        print(f"{self.__class__.__name__} leveled up! Stats increased.")

    

class Wizard(System):
    def __init__(self, level = 1, experience = 0, healthpoint=80, attack=15, defense=8, m_defense=12, mana=30, speed=12):
        super().__init__(level, healthpoint, experience, attack, defense, m_defense, mana, speed)
    
    
class Rogue(System):
    def __init__(self, level = 1, experience = 0, healthpoint=90, attack=18, defense=12, m_defense=20, mana=10, speed=15):
        super().__init__(level, healthpoint, experience, attack, defense, m_defense, mana, speed)
     

class Archer(System):
    def __init__(self, level = 1, experience = 0, healthpoint=85, attack=17, defense=10, m_defense=18, mana=8, speed=14):
        super().__init__(level, healthpoint, experience, attack, defense, m_defense, mana, speed)
        
        