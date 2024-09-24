# Step one creating The system
# Established stats
# Created Leveling System
class System:
    def __init__(self, level, base_health, base_attack, base_m_attack, base_defense, base_m_defense, base_mana, base_speed):
        self.level = level
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_m_attack = base_m_attack
        self.base_defense = base_defense
        self.base_m_defense = base_m_defense
        self.base_mana = base_mana
        self.base_speed = base_speed
        self.update_stats()

    def update_stats(self):
        self.health = self.base_health + (self.level - 1) * self.health_gain()
        self.attack = self.base_attack + (self.level - 1) * self.attack_gain()
        self.m_attack = self.base_m_attack + (self.level - 1) * self.m_attack_gain()
        self.defense = self.base_defense + (self.level - 1) * self.defense_gain()
        self.m_defense = self.base_m_defense + (self.level - 1) * self.m_defense_gain()
        self.mana = self.base_mana + (self.level - 1) * self.mana_gain()
        self.speed = self.base_speed + (self.level - 1) * self.speed_gain()

    def health_gain(self):
        return 0

    def attack_gain(self):
        return 0

    def m_attack_gain(self):
        return 0

    def defense_gain(self):
        return 0

    def m_defense_gain(self):
        return 0

    def mana_gain(self):
        return 0

    def speed_gain(self):
        return 0

    def __str__(self):
        return (f"{self.__class__.__name__}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Attack: {self.attack}\n"
                f"Magic Attack: {self.m_attack}\n"
                f"Defense: {self.defense}\n"
                f"Magic Defense: {self.m_defense}\n"
                f"Mana: {self.mana}\n"
                f"Speed: {self.speed}\n"
                f"Moves:\n{self.format_moves()}")

    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())