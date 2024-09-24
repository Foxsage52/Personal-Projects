from System import System
from moves import universal_moves
import moves
from blocking import Block

class Warrior(System):
    def __init__(self, level=1):
        base_stats = {
            'base_health': 100,
            'base_attack': 20,
            'base_m_attack': 5,
            'base_defense': 15,
            'base_m_defense': 10,
            'base_mana': 5,
            'base_speed': 10
        }
        super().__init__(level, **base_stats)
        self.moves = {**moves.warrior_moves.copy(), **universal_moves, 'Block': Block.block_move()}
        moves.update_warrior_moves(self)

    def health_gain(self):
        return 25

    def attack_gain(self):
        return 20

    def m_attack_gain(self):
        return 10

    def defense_gain(self):
        return 20

    def m_defense_gain(self):
        return 10

    def mana_gain(self):
        return 5

    def speed_gain(self):
        return 10

    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())

class Wizard(System):
    def __init__(self, level=1):
        base_stats = {
            'base_health': 80,
            'base_attack': 15,
            'base_m_attack': 30,
            'base_defense': 8,
            'base_m_defense': 12,
            'base_mana': 30,
            'base_speed': 12
        }
        super().__init__(level, **base_stats)
        self.moves = {**moves.wizard_moves.copy(), **universal_moves, 'Block': Block.block_move()}
        moves.update_wizard_moves(self)

    def health_gain(self):
        return 15

    def attack_gain(self):
        return 20

    def m_attack_gain(self):
        return 25

    def defense_gain(self):
        return 10

    def m_defense_gain(self):
        return 10

    def mana_gain(self):
        return 10

    def speed_gain(self):
        return 8

    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())

class Rogue(System):
    def __init__(self, level=1):
        base_stats = {
            'base_health': 90,
            'base_attack': 18,
            'base_m_attack': 10,
            'base_defense': 12,
            'base_m_defense': 20,
            'base_mana': 10,
            'base_speed': 15
        }
        super().__init__(level, **base_stats)
        self.moves = {**moves.rogue_moves.copy(), **universal_moves, 'Block': Block.block_move()}
        moves.update_rogue_moves(self)

    def health_gain(self):
        return 18

    def attack_gain(self):
        return 15

    def m_attack_gain(self):
        return 15

    def defense_gain(self):
        return 15

    def m_defense_gain(self):
        return 15

    def mana_gain(self):
        return 10

    def speed_gain(self):
        return 15

    def format_moves(self):
        return "\n".join(f"{name}: {details}" for name, details in self.moves.items())