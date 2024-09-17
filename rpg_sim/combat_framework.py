class Combat:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def attack(self, move_name):
        if move_name not in self.attacker.moves:
            return f"{self.attacker.__class__.__name__} does not have the move '{move_name}'"

        move = self.attacker.moves[move_name]
        
        if move["type"] == "special":
            cost = move.get("cost", 0)  # Provide a default value of 0 if "cost" is not specified
            if self.attacker.mana < cost:
                return f"{self.attacker.__class__.__name__} does not have enough mana for '{move_name}'"
            self.attacker.mana -= cost
            damage = self.calculate_damage(move["power"], self.attacker.m_attack)
        else:
            damage = self.calculate_damage(move["power"], self.attacker.attack)
            self.attacker.mana += move.get("regen", 1)  # Default regen to 1 if not specified

        self.defender.healthpoint -= damage
        return (f"{self.attacker.__class__.__name__} used '{move_name}' on {self.defender.__class__.__name__}. "
                f"{self.defender.__class__.__name__}'s health is now {self.defender.healthpoint:.2f}. "
                f"{self.attacker.__class__.__name__}'s mana is now {self.attacker.mana}.")
    
    def calculate_damage(self, move_power, attack_stat):
        # Basic damage calculation formula
        return move_power + attack_stat * 0.5
