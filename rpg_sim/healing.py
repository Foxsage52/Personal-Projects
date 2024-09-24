# healing.py

from classes import Warrior, Wizard, Rogue  # For healing moves applicable to these character types.

def healing(attacker, move, move_name):
    """Handles healing for player characters."""
    max_health = attacker.base_health + (attacker.level - 1) * attacker.health_gain()
    max_mana = attacker.base_mana + (attacker.level - 1) * attacker.mana_gain()
    heal_percent = move.get("heal_percent", 0) / 100
    heal_amount = max_health * heal_percent
    mana_restore = max_mana * heal_percent
    mana_cost = move.get("cost", 0)

    if attacker.mana < mana_cost:
        return f"{attacker.__class__.__name__} does not have enough mana to use '{move_name}'."

    # Deduct mana cost
    attacker.mana -= mana_cost

    # Ensure healing does not exceed max health and mana
    attacker.health = min(attacker.health + heal_amount, max_health)
    attacker.mana = min(attacker.mana + mana_restore, max_mana)
    
    return (f"{attacker.__class__.__name__} used '{move_name}'. "
            f"Restored {heal_amount:.2f} HP and {mana_restore:.2f} Mana! "
            f"{attacker.__class__.__name__}'s health is now {attacker.health:.2f} and mana is now {attacker.mana:.2f}.")