import random
import json

def generate_data(num_tasks=10001, max_time=100, max_dependencies=15000, num_machines_range=(0, 1000+1)):
    """
    Generate JSON data with random execution times, dependencies, and the number of machines.
    
    Parameters:
        num_tasks (int): Number of tasks to generate.
        max_time (int): Maximum execution time for a task.
        max_dependencies (int): Maximum number of dependencies to generate.
        num_machines_range (tuple): Range for random number of machines (min, max).

    Returns:
        dict: Generated data.
    """
    # Generate random execution times for tasks
    execution_times = [random.randint(1, max_time) for _ in range(num_tasks)]

    # Generate random dependencies between tasks
    dependencies = []
    for _ in range(random.randint(1, max_dependencies)):
        task_a = random.randint(0, num_tasks - 1)
        task_b = random.randint(0, num_tasks - 1)
        if task_a != task_b:
            dependencies.append([task_a, task_b])

    # Generate a random number of machines within the specified range
    num_machines = random.randint(*num_machines_range)

    return {
        "execution_times": execution_times,
        "dependencies": dependencies,
        "num_machines": num_machines
    }

# Generate the data with default or custom parameters
data = generate_data(num_tasks=10000, max_time=100, max_dependencies=15000, num_machines_range=(2, 4))

# Convert the data to JSON format
file_path = "input.json"
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

# Save or print the generated JSON data
