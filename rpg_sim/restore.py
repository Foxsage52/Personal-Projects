def restore_health(enemy):
    """Handles the 'Restore' move for enemies."""
    heal_percent = enemy.moves.get("Restore", {}).get("heal_percent", 25)
    restore_amount = enemy._max_health() * (heal_percent / 100)
    health_before = enemy.healthpoint

    # Ensure health is capped at max health
    enemy.healthpoint = min(health_before + restore_amount, enemy._max_health())

    return (f"{enemy.name} used 'Restore'. Restored {restore_amount:.2f} HP! "
            f"{enemy.name}'s health is now {enemy.healthpoint:.2f}.")
