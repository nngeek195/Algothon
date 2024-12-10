import subprocess

# List of Python files you want to run
files = ['main1.py', 'loop.py']

# Run each file multiple times
for _ in range(3):  # Change 3 to however many times you want
    for file in files:
        subprocess.run(['python', file])  # Executes the script
