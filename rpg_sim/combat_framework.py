from classes import Warrior, Wizard, Rogue

class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def attack(self, move_name):
        if move_name not in self.attacker.moves:
            return f"{self.attacker.__class__.__name__} does not have the move '{move_name}'"

        move = self.attacker.moves[move_name]
        is_special = (move["type"] == "special")

        if is_special:
            cost = move.get("cost", 0)  # Provide a default value of 0 if "cost" is not specified
            if self.attacker.mana < cost:
                return f"{self.attacker.__class__.__name__} does not have enough mana for '{move_name}'"
            self.attacker.mana -= cost
        else:
            self.attacker.mana += move.get("regen", 1)  # Default regen to 1 if not specified

        if move["type"] == "heal":
            return self.heal(move)

        # Calculate damage based on class-specific mechanics and defense mitigation
        damage = self.calculate_damage(move["power"], is_special)
        self.defender.healthpoint -= damage

        return (f"{self.attacker.__class__.__name__} used '{move_name}' on {self.defender.__class__.__name__}. "
                f"It dealt {damage:.2f} damage! "
                f"{self.defender.__class__.__name__}'s health is now {self.defender.healthpoint:.2f}. "
                f"{self.attacker.__class__.__name__}'s mana is now {self.attacker.mana:.2f}.")

    def heal(self, move):
        heal_amount = self.attacker._max_health() * (move.get("heal", 0) / 100)

        # Ensure healing does not exceed maximum health
        self.attacker.healthpoint = min(self.attacker.healthpoint + heal_amount, self.attacker._max_health())
        return (f"{self.attacker.__class__.__name__} used '{move.get('name', 'Heal')}'. "
                f"Restored {heal_amount:.2f} HP! {self.attacker.__class__.__name__}'s health is now {self.attacker.healthpoint:.2f}. "
                f"{self.attacker.__class__.__name__}'s mana is now {self.attacker.mana:.2f}.")

    def calculate_damage(self, attack_power, is_special=False):
        # Flat reduction based on defense (defense / 2)
        flat_reduction = self.defender.defense / 2

        # Calculate base damage based on class and type of attack
        if isinstance(self.attacker, Warrior):
            if is_special:
                base_damage = (self.attacker.attack + attack_power * 1.5)  # 1.5 ratio for special attacks
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

        # Apply flat reduction
        damage_after_flat = base_damage - flat_reduction

        # Cap defense reduction at 70% (minimum 30% of damage must go through)
        final_damage = max(damage_after_flat, 0) * max(0.3, 1 - (self.defender.defense / 200))

        # Ensure damage can't be lower than a minimum threshold (optional)
        min_damage = 5  # Set a minimum damage threshold if needed
        return max(final_damage, min_damage)
