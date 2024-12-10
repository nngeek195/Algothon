import subprocess

# List of Python files you want to run
files = ['file1.py', 'file2.py']

# Run each file multiple times
for _ in range(3):  # Change 3 to however many times you want
    for file in files:
        subprocess.run(['python', file])  # Executes the script
