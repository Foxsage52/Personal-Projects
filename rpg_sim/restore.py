
def restore(enemy):
    """Handles the 'Restore' move for enemies."""
    restore_amount = enemy._max_health() * (enemy.moves["Restore"].get("heal_percent", 25) / 100)
    enemy.healthpoint = min(enemy.healthpoint + restore_amount, enemy._max_health())
    return (f"{enemy.name} used 'Restore'. Restored {restore_amount:.2f} HP! {enemy.name}'s health is now {enemy.healthpoint:.2f}.")
