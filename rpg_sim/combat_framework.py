class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def calculate_damage(self, attack_power, is_special=False):
        # Assuming basic and special move power adjustments
        if is_special:
            damage = (self.attacker.attack * (attack_power * 0.5)) * (1 - (self.defender.defense / 100))
        else:
            damage = (self.attacker.attack + attack_power) * (1 - (self.defender.defense / 100))
        return damage

    def attack(self, move_name):
        move = self.attacker.moves.get(move_name, {})
        if move:
            power = move.get("power", 0)
            is_special = move.get("type") == "special"
            damage = self.calculate_damage(power, is_special)
            self.defender.healthpoint -= damage
            return f"{self.attacker.__class__.__name__} attacked with {move_name}, dealing {damage} damage!"
        return "Invalid move"

