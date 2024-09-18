# Import mechanics from existing files like healing, restore, attack, etc.
import healing  # Manages healing logic
import restore  # Manages restore logic
import attack   # Manages attack logic

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
            
            if move["type"] == "attack":
                return self.execute_attack(move)
            elif move["type"] == "heal":
                return self.execute_heal(move)
            elif move["type"] == "restore":
                return self.execute_restore(move)
            else:
                return "Unknown move type."
        else:
            return f"{self.attacker.__class__.__name__} doesn't know '{move_name}'"

    def execute_attack(self, move):
        damage = attack.calculate_damage(self.attacker, self.defender, move)
        self.defender.healthpoint -= damage
        return f"{self.attacker.__class__.__name__} dealt {damage:.2f} damage to {self.defender.__class__.__name__}. Health remaining: {self.defender.healthpoint:.2f}"

    def execute_heal(self, move):
        heal_amount = healing.calculate_heal(self.attacker, move)
        return f"{self.attacker.__class__.__name__} healed for {heal_amount:.2f} HP."

    def execute_restore(self, move):
        restore_amount = restore.calculate_restore(self.attacker, move)
        return f"{self.attacker.__class__.__name__} restored {restore_amount:.2f} mana."

