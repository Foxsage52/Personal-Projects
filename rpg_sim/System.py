#Step one creating The system
#Establihsed stats
#Created Leveling Sysetm
class System:
    def __init__(self, level, healthpoint, experience, attack, defense, m_defense, mana, speed):
        self.level = level         # Class level
        self.healthpoint = healthpoint  # Hit points
        self.experience = experience    # Level progress
        self.attack = attack       # Attack Power
        self.defense = defense     # Defensive prowess
        self.m_defense = m_defense             # Magic Defense
        self.mana = mana           # Special Resource
        self.speed = speed         # Turn order
        self.moves = {}

    
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
                f"Speed: {self.speed}\n"
                f"Moves:\n{self.format_moves()}")
                
    
    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())
