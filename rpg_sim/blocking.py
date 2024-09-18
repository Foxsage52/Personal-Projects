class Block:
    def __init__(self, blocker):
        self.blocker = blocker

    def execute(self):
        # Block logic: regenerate mana and enhance defense for the turn
        regen_amount = 0
        self.blocker.mana += regen_amount
        
        # Add damage mitigation by increasing defense and magic defense temporarily
        block_defense_boost = self.blocker.defense * 0.5
        block_m_defense_boost = self.blocker.m_defense * 0.5
        
        return (f"{self.blocker.__class__.__name__} used Block. "
                f"{self.blocker.__class__.__name__}'s mana is now {self.blocker.mana:.2f}. "
                f"Defense increased by {block_defense_boost:.2f} and Magic Defense increased by {block_m_defense_boost:.2f} for this turn.")

    @staticmethod
    def block_move():
        # Return the move details for Block
        return {"type": "block", "power": 0}
