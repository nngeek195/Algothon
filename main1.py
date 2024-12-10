import json
from collections import deque, defaultdict
import heapq

# Step 1: Topological Sorting using Kahn's Algorithm
def topological_sort(num_jobs, dependencies):
    # Initialize graph and in-degrees
    graph = defaultdict(list)
    in_degree = [0] * num_jobs

    for u, v in dependencies:
        graph[u].append(v)
        in_degree[v] += 1

    # Queue for jobs with no dependencies
    queue = deque([i for i in range(num_jobs) if in_degree[i] == 0])
    top_order = []

    while queue:
        job = queue.popleft()
        top_order.append(job)
        for neighbor in graph[job]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) == num_jobs:
        return top_order
    else:
        raise ValueError("Cycle detected in the dependency graph.")

# Step 2: Schedule Jobs on Machines
def schedule_jobs(num_jobs, execution_times, top_order, num_machines):
    # Min-heap to track next available time of each machine
    machine_heap = [(0, i) for i in range(num_machines)]  # (time, machine_id)
    heapq.heapify(machine_heap)

    # Track job completion times
    job_completion_time = [0] * num_jobs

    for job in top_order:
        earliest_time, machine_id = heapq.heappop(machine_heap)
        start_time = earliest_time
        finish_time = start_time + execution_times[job]
        job_completion_time[job] = finish_time

        # Update machine availability
        heapq.heappush(machine_heap, (finish_time, machine_id))

    # Makespan is the maximum finish time of all jobs
    makespan = max(job_completion_time)
    return makespan, job_completion_time

# Main Function
def minimize_makespan(num_jobs, execution_times, dependencies, num_machines):
    # Step 1: Perform topological sorting
    top_order = topological_sort(num_jobs, dependencies)
    
    # Step 2: Schedule jobs on machines
    makespan, job_completion_time = schedule_jobs(num_jobs, execution_times, top_order, num_machines)
    
    return makespan, job_completion_time

if __name__ == "__main__":
    # Load input data from JSON file
    input_file = "input.json"  # Replace with your JSON file name
    try:
        with open(input_file, "r") as file:
            data = json.load(file)

        # Extract data from JSON
        execution_times = data["execution_times"]
        dependencies = data["dependencies"]
        num_machines = data["num_machines"]
        num_jobs = len(execution_times)

        # Run the algorithm
        makespan, job_completion_time = minimize_makespan(num_jobs, execution_times, dependencies, num_machines)

        # Output the results
        print("Makespan:", makespan)
        print("Job Completion Times:", job_completion_time)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from '{input_file}'.")
    except ValueError as e:
        print(e)