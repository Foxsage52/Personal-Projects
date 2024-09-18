from classes import Warrior, Wizard, Rogue  # Import only the classes used for attack logic.

class Attack:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def perform_attack(self, move_name):
        """Performs an attack based on the chosen move."""
        if move_name not in self.attacker.moves:
            return f"{self.attacker.__class__.__name__} does not have the move '{move_name}'"

        move = self.attacker.moves[move_name]
        is_special = (move["type"] == "special")

        if is_special:
            cost = move.get("cost", 0)
            if self.attacker.mana < cost:
                return f"{self.attacker.__class__.__name__} does not have enough mana for '{move_name}'"
            self.attacker.mana -= cost
        else:
            # Regenerate mana for normal attacks
            self.attacker.mana += move.get("regen", 1)

        # Calculate damage and apply to defender
        damage = self.calculate_damage(move["power"], is_special)
        self.defender.healthpoint -= damage

        return (f"{self.attacker.__class__.__name__} used '{move_name}' on {self.defender.__class__.__name__}. "
                f"It dealt {damage:.2f} damage! "
                f"{self.defender.__class__.__name__}'s health is now {self.defender.healthpoint:.2f}. "
                f"{self.attacker.__class__.__name__}'s mana is now {self.attacker.mana:.2f}.")

    def calculate_damage(self, attack_power, is_special=False):
        """Calculates damage based on class-specific mechanics and defense."""
        flat_reduction = self.defender.defense / 2

        if isinstance(self.attacker, Warrior):
            if is_special:
                base_damage = (self.attacker.attack + attack_power * 1.5)  # 1.5x power for special attacks
            else:
                base_damage = self.attacker.attack + attack_power

        elif isinstance(self.attacker, Wizard):
            if is_special:
                base_damage = (self.attacker.m_attack * 1.0) + (attack_power * 1.0)
            else:
                base_damage = (self.attacker.m_attack * 0.5) + (self.attacker.attack * 0.5) + attack_power

        elif isinstance(self.attacker, Rogue):
            if is_special:
                base_damage = (self.attacker.m_attack * 0.75) + (self.attacker.attack * 0.75) + attack_power
            else:
                base_damage = (self.attacker.m_attack * 0.75) + (self.attacker.attack * 0.75) + attack_power

        else:
            base_damage = self.attacker.attack + attack_power

        # Apply defense reduction
        damage_after_flat = base_damage - flat_reduction
        final_damage = max(damage_after_flat, 0) * max(0.3, 1 - (self.defender.defense / 200))

        # Minimum damage threshold
        min_damage = 5
        return max(final_damage, min_damage)
