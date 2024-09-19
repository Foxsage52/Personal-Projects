import random
from restore import restore_health

class Enemy:
    def __init__(self, name, player, base_healthpoint, base_attack, base_defense, base_speed, base_mana=0, moves=None):
        self.name = name
        self.level = player.level + 1  # Always a level higher than the player

        # Calculate scaling factor based on player's current stats
        self.scaling_factor = random.uniform(1.1, 1.5)  # Store this for later use

        # Adjust enemy stats relative to the player's stats
        self.healthpoint = base_healthpoint * self.scaling_factor
        self.attack = base_attack * self.scaling_factor
        self.defense = base_defense * self.scaling_factor
        self.mana = base_mana * self.scaling_factor
        self.speed = base_speed * self.scaling_factor

        # Ensure stats are sufficiently higher than the player's
        self.healthpoint = max(self.healthpoint, player.healthpoint * 1.1)
        self.attack = max(self.attack, player.attack * 1.1)
        self.defense = max(self.defense, player.defense * 1.1)
        self.mana = max(self.mana, player.mana * 1.1)
        self.speed = max(self.speed, player.speed * 1.1)

        # Add restore move
        self.moves = moves if moves is not None else {}
        self.moves["Restore"] = {"power": 0, "type": "special", "heal_percent": 25}
        self.heal_uses = 2  # Limit of 2 uses for the restore move

    def choose_move(self):
        """Choose a move based on the enemy's current health and restore uses."""
        max_health = self._max_health()  # Get the maximum health value
        health_percentage = self.healthpoint / max_health  # Calculate health percentage

        print(f"Debug: {self.name}'s current health: {self.healthpoint:.2f}, max health: {max_health:.2f}, health percentage: {health_percentage:.2f}")

        if health_percentage <= 0.25 and self.heal_uses > 0:
            self.heal_uses -= 1
            return restore_health(self)  # Call the restore health function
        
        normal_moves = [move for move in self.moves if self.moves[move]["type"] == "normal"]
        special_moves = [move for move in self.moves if self.moves[move]["type"] == "special"]

        if special_moves:
            return random.choice(special_moves)
        
        return random.choice(normal_moves)

    def _max_health(self):
        """Calculate max health based on scaling factor for comparison purposes."""
        return self.healthpoint / self.scaling_factor

    def __str__(self):
        """Provide a string representation of the enemy."""
        return (f"{self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.healthpoint:.2f}\n"
                f"Attack: {self.attack:.2f}\n"
                f"Defense: {self.defense:.2f}\n"
                f"Mana: {self.mana:.2f}\n"
                f"Speed: {self.speed:.2f}\n"
                f"Moves: {', '.join(self.moves.keys())}")


class Goblin(Enemy):
    def __init__(self, player):
        super().__init__(
            name="Goblin",
            player=player,
            base_healthpoint=60,
            base_attack=12,
            base_defense=6,
            base_speed=6,
            moves={
                "Slash": {"power": 5, "type": "normal"},
                "Bite": {"power": 7, "type": "normal"}
            }
        )

class Orc(Enemy):
    def __init__(self, player):
        super().__init__(
            name="Orc",
            player=player,
            base_healthpoint=90,
            base_attack=18,
            base_defense=12,
            base_speed=6,
            moves={
                "Club Smash": {"power": 10, "type": "normal"},
                "Roar": {"power": 0, "type": "special"}
            }
        )

class Dragon(Enemy):
    def __init__(self, player):
        super().__init__(
            name="Dragon",
            player=player,
            base_healthpoint=140,
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
