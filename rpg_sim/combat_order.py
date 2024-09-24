# combat_order.py

import random
from attack import Attack
from blocking import Block
from healing import healing
from enemy import Enemy

class CombatSystem:
    def __init__(self, user, enemy):
        self.user = user
        self.enemy = enemy
        self.block_active = False

    def user_turn(self, move_name):
        # Handle user's move, including attack, block, or healing
        if move_name == "Block":
            block = Block(self.user)
            self.block_active = True
            return block.execute()

        elif move_name in ["Invigorating Shout", "Restore Body", "Blood Bath"]:
            heal_move = self.user.moves.get(move_name)
            if heal_move:
                return healing(self.user, heal_move, move_name)
            else:
                return f"{self.user.__class__.__name__} cannot use '{move_name}'"

        elif move_name in self.user.moves:
            attack = Attack(self.user, self.enemy)
            return attack.perform_attack(move_name)
        else:
            return f"Invalid move choice: {move_name}"

    def enemy_turn(self):
        # Determine if the enemy's attack misses based on relative speeds
        speed_difference = self.user.speed - self.enemy.speed
        base_miss_chance = 0.33
        miss_chance = base_miss_chance + (speed_difference / 100)

        if random.random() < miss_chance:
            return f"{self.enemy.name} tried to attack but missed!"

        # Enemy chooses a move (random or based on logic) and attacks
        chosen_move = self.enemy.choose_move()
        attack = Attack(self.enemy, self.user)
        return attack.perform_attack(chosen_move)

    def combat_round(self, user_move):
        # One full round of combat: user turn and enemy turn
        user_action = self.user_turn(user_move)
        if self.enemy.health <= 0:
            return f"{self.enemy.name} has been defeated! {user_action}"

        enemy_action = self.enemy_turn()
        if self.user.health <= 0:
            return f"{self.user.__class__.__name__} has been defeated! {enemy_action}"

        # Reset defense values if Block was used
        if self.block_active:
            block = Block(self.user)
            block.reset_defense()
            self.block_active = False

        return f"User Turn:\n{user_action}\n\nEnemy Turn:\n{enemy_action}"

    def is_combat_over(self):
        return self.user.health <= 0 or self.enemy.health <= 0