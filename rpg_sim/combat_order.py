# combat_order.py

import healing  # Manages healing logic
import restore  # Manages restore logic
from attack import Attack

class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def take_turn(self, move_name):
        """
        Determines the move for the attacker and applies it.
        Handles whether the move is an attack, heal, or restore.
        """
        if move_name in self.attacker.moves:
            move = self.attacker.moves[move_name]
            
            if move["type"] == "basic" or move["type"] == "special":
                return self.execute_attack(move_name)
            elif move["type"] == "heal":
                return self.execute_heal(move)
            elif move["type"] == "restore":
                return self.execute_restore(move)
            else:
                return "Unknown move type."
        else:
            return f"{self.attacker.__class__.__name__} doesn't know '{move_name}'"

    def execute_attack(self, move_name):
        move = self.attacker.moves[move_name]
        attack_system = Attack(self.attacker, self.defender)
        result = attack_system.perform_attack(move_name)
        return result

    def execute_heal(self, move):
        heal_amount = healing.calculate_heal(self.attacker, move)
        return f"{self.attacker.__class__.__name__} healed for {heal_amount:.2f} HP."

    def execute_restore(self, move):
        restore_amount = restore.calculate_restore(self.attacker, move)
        return f"{self.attacker.__class__.__name__} restored {restore_amount:.2f} mana."
