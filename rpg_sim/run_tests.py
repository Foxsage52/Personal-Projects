import subprocess

for i in range(10):  # Adjust the range for the number of runs you want
    print(f"Run {i+1}")
    subprocess.run(["python", "rpg_sim/combat_test.py"])  # Adjust the path as needed
    print("\n")