# blocking.py

class Block:
    def __init__(self, character):
        self.character = character
        self.original_defense = character.defense
        self.original_m_defense = character.m_defense

    def execute(self):
        # Store the current defense values before increasing them
        self.character.temp_defense = self.character.defense
        self.character.temp_m_defense = self.character.m_defense

        # Increase defense and magic defense for this turn
        print(f"DEBUG: Before Block - Defense: {self.character.defense}, Magic Defense: {self.character.m_defense}")
        self.character.defense += self.original_defense * 0.5
        self.character.m_defense += self.original_m_defense * 0.5
        print(f"DEBUG: After Block - Defense: {self.character.defense}, Magic Defense: {self.character.m_defense}")
        return (f"{self.character.__class__.__name__} used Block. "
                f"{self.character.__class__.__name__}'s mana is now {self.character.mana:.2f}. "
                f"Defense increased by {self.original_defense * 0.5:.2f} and Magic Defense increased by {self.original_m_defense * 0.5:.2f} for this turn.")

    def reset_defense(self):
        # Reset defense and magic defense to the stored values
        print(f"DEBUG: Before Reset - Defense: {self.character.defense}, Magic Defense: {self.character.m_defense}")
        self.character.defense = self.character.temp_defense
        self.character.m_defense = self.character.temp_m_defense
        print(f"DEBUG: After Reset - Defense: {self.character.defense}, Magic Defense: {self.character.m_defense}")

    @staticmethod
    def block_move():
        return {"type": "block", "power": 0}