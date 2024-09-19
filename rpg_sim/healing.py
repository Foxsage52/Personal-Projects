from classes import Warrior, Wizard, Rogue  # For healing moves applicable to these character types.

def healing(attacker, move):
    """Handles healing for player characters."""
    heal_amount = attacker._max_health() * (move.get("heal", 0) / 100)

    # Ensure healing does not exceed max health
    attacker.healthpoint = min(attacker.healthpoint + heal_amount, attacker._max_health())
    return (f"{attacker.__class__.__name__} used '{move.get('name', 'Heal')}'. "
            f"Restored {heal_amount:.2f} HP! {attacker.__class__.__name__}'s health is now {attacker.healthpoint:.2f}.")
