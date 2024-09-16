from System import System
import moves

class Warrior(System):
    def __init__(self, level=1, experience=0, healthpoint=100, attack=20, m_attack=5, defense=15, m_defense=10, mana=5, speed=10):
        super().__init__(level, healthpoint, experience, attack, m_attack, defense, m_defense, mana, speed)
        self.m_attack = m_attack
        self.moves = moves.warrior_moves.copy()
        moves.update_warrior_moves(self)

    def level_up(self):
        super().level_up()
        self.healthpoint += 15
        self.attack += 10
        self.defense += 5
        self.m_attack += 2
        self.m_defense += 3
        self.mana += 4
        self.speed += 5
        print(f"{self.__class__.__name__} leveled up! Stats increased.")
        moves.update_warrior_moves(self)

    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())

class Wizard(System):
    def __init__(self, level=1, experience=0, healthpoint=80, attack=15, m_attack=30, defense=8,  m_defense=12, mana=30, speed=12):
        super().__init__(level, healthpoint, experience, attack, m_attack, defense, m_defense, mana, speed)
        self.m_attack = m_attack

class Rogue(System):
    def __init__(self, level=1, experience=0, healthpoint=90, attack=18, m_attack=10, defense=12, m_defense=20, mana=10, speed=15):
        super().__init__(level, healthpoint, experience, attack, m_attack, defense, m_defense, mana, speed)
        self.m_attack = m_attack

class Archer(System):
    def __init__(self, level=1, experience=0, healthpoint=85, attack=17, m_attack=8, defense=10, m_defense=18, mana=8, speed=14):
        super().__init__(level, healthpoint, experience, attack, m_attack, defense, m_defense, mana, speed)
        self.m_attack = m_attack
