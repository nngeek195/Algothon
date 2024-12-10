import subprocess

# List of Python files you want to run
files = ['algorithm.py', 'loop.py']

times = int(input())
# Run each file multiple times
for _ in range(times):  # Change 3 to however many times you want
    for file in files:
        subprocess.run(['python', file])  # Executes the script
