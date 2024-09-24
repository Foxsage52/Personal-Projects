import random

class Enemy:
    def __init__(self, name, player, base_health, base_attack, base_defense, base_speed, base_mana=0, moves=None):
        self.name = name
        self.level = player.level + 1  # Always a level higher than the player

        # Fixed scaling factor
        self.scaling_factor = 1.1

        # Adjust enemy stats relative to the player's stats and round to the nearest whole number
        self.max_health = round(player.health * self.scaling_factor)
        self.health = self.max_health
        self.attack = round(player.attack * self.scaling_factor)
        self.defense = round(player.defense * self.scaling_factor)
        self.mana = round(player.mana * self.scaling_factor)
        self.speed = round(player.speed * self.scaling_factor)

        # Add moves
        self.moves = moves if moves is not None else {}

    def choose_move(self):
        """Choose a random move."""
        print(f"{self.name} is choosing a random move. Current health: {self.health}, Max health: {self.max_health}")
        return random.choice(list(self.moves.keys()))

    def health_percentage(self):
        return self.health / self.max_health

    def __str__(self):
        return (f"{self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Attack: {self.attack}\n"
                f"Defense: {self.defense}\n"
                f"Mana: {self.mana}\n"
                f"Speed: {self.speed}\n"
                f"Moves: {', '.join(self.moves.keys())}")

    def _max_health(self):
        return self.max_health

class Goblin(Enemy):
    def __init__(self, player):
        super().__init__("Goblin", player, base_health=100, base_attack=20, base_defense=15, base_speed=10, base_mana=5, moves={"Slash": {"power": 10, "type": "physical"}, "Bite": {"power": 15, "type": "physical"}})

class Orc(Enemy):
    def __init__(self, player):
        super().__init__("Orc", player, base_health=120, base_attack=25, base_defense=18, base_speed=12, base_mana=10, moves={"Club Smash": {"power": 20, "type": "physical"}, "Roar": {"power": 0, "type": "special"}})

class Dragon(Enemy):
    def __init__(self, player):
        super().__init__(
            name="Dragon",
            player=player,
            base_health=140,
            base_attack=24,
            base_defense=20,
            base_speed=6,
            base_mana=50,
            moves={
                "Fire Breath": {"power": 20, "type": "special"},
                "Claw Strike": {"power": 15, "type": "normal"},
                "Tail Whip": {"power": 12, "type": "normal"}
            }
        )