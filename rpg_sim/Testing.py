import classes

# Create a Warrior instance
warrior = classes.Warrior()

# Print initial state
print(warrior)
print("")

# Simulate gaining experience
warrior.gain_experience(500)

# Print updated state
print(warrior)
print("")

wizard = classes.Wizard()

print(wizard)
print("")

wizard.gain_experience(500)
print(wizard)