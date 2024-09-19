from attack import Attack
from blocking import Block
from healing import healing
from enemy import Enemy
from restore import restore_health

class CombatSystem:
    def __init__(self, user, enemy):
        self.user = user
        self.enemy = enemy

    def user_turn(self, move_name):
        # Handle user's move, including attack, block, or healing
        if move_name == "Block":
            block = Block(self.user)
            return block.execute()

        elif move_name == "Heal":
            heal_move = self.user.moves.get("Heal")
            if heal_move:
                return healing(self.user, heal_move)
            else:
                return f"{self.user.__class__.__name__} cannot use 'Heal'"

        elif move_name in self.user.moves:
            attack = Attack(self.user, self.enemy)
            return attack.perform_attack(move_name)
        else:
            return f"Invalid move choice: {move_name}"

    def enemy_turn(self):
        # Enemy chooses a move (random or based on logic) and attacks
        chosen_move = self.enemy.choose_move()
        if chosen_move == "Restore":
            return restore_health(self.enemy)
        else:
            attack = Attack(self.enemy, self.user)
            return attack.perform_attack(chosen_move)

    def combat_round(self, user_move):
        # One full round of combat: user turn and enemy turn
        user_action = self.user_turn(user_move)
        if self.enemy.healthpoint <= 0:
            return f"{self.enemy.name} has been defeated! {user_action}"

        enemy_action = self.enemy_turn()
        if self.user.healthpoint <= 0:
            return f"{self.user.__class__.__name__} has been defeated! {enemy_action}"

        return f"User Turn:\n{user_action}\n\nEnemy Turn:\n{enemy_action}"

    def is_combat_over(self):
        return self.user.healthpoint <= 0 or self.enemy.healthpoint <= 0
