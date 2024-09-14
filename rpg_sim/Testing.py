import Classes

wizard = Classes.Wizard(level= 1, experience = 0, healthpoint = 10, attack = 10, defense = 5, mana = 10, dex = 20, speed = 15)

wizard.gain_experience(20)
print(wizard)