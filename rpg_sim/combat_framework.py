class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def calculate_damage(self, attack_power, is_special=False):
        # Flat reduction based on defense (defense / 2)
        flat_reduction = self.defender.defense / 2
        
        # Calculate base damage based on whether it's a special move or not
        if is_special:
            base_damage = self.attacker.attack * attack_power
        else:
            base_damage = self.attacker.attack + attack_power
        
        # Apply flat reduction
        damage_after_flat = base_damage - flat_reduction

        # Cap defense reduction at 70% (minimum 30% of damage must go through)
        final_damage = max(damage_after_flat, 0) * max(0.3, 1 - (self.defender.defense / 200))

        # Ensure damage can't be lower than a minimum threshold (optional)
        min_damage = 5  # Set a minimum damage threshold if needed
        return max(final_damage, min_damage)

    def attack(self, move_name):
        move = self.attacker.moves.get(move_name, {})
        if move:
            power = move.get("power", 0)
            is_special = move.get("type") == "special"
            damage = self.calculate_damage(power, is_special)
            self.defender.healthpoint -= damage
            return f"{self.attacker.__class__.__name__} attacked with {move_name}, dealing {damage:.2f} damage!"
        return "Invalid move"
