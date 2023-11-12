from tabulate import tabulate

def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(burst_time)
    
    # Convert process names to letters A, B, C, ...
    process_names = [chr(65 + i) for i in range(n)]
    
    # Initialize waiting time and turnaround time arrays
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Initialize remaining time for each process
    remaining_time = burst_time.copy()
    
    # Initialize the time variable to keep track of current time
    time = 0
    
    # Initialize queue to store the processes
    queue = []
    
    # Initialize Gantt chart strings
    gantt_chart = ""
    gantt_chart_numbers = ""
    
    # Continue processing until all processes are done
    while any(remaining_time):
        for i in range(n):
            if remaining_time[i] > 0 and arrival_time[i] <= time:
                if remaining_time[i] <= quantum:
                    time += remaining_time[i]
                    waiting_time[i] = time - burst_time[i] - arrival_time[i]
                    remaining_time[i] = 0
                else:
                    time += quantum
                    remaining_time[i] -= quantum
                turnaround_time[i] = time - arrival_time[i]
                queue.append(process_names[i])
                gantt_chart += f"{process_names[i]:^3}"
                gantt_chart_numbers += f"{time:^3}"
                
    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    # Create a table for input and output data
    table_data = list(zip(process_names, burst_time, arrival_time, waiting_time, turnaround_time))
    headers = ["Process", "Burst Time", "Arrival Time", "Waiting Time", "Turnaround Time"]
    input_output_table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    
    # Print the table and other results
    print("Input and Output Data:")
    print(input_output_table)
    print("\nGantt Chart:")
    print(gantt_chart)
    print(gantt_chart_numbers)
    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

# Input from the user
burst_time = list(map(int, input("Enter burst times (separated by space): ").split()))
arrival_time = list(map(int, input("Enter arrival times (separated by space): ").split()))
quantum = int(input("Enter time quantum: "))

# Run the Round Robin algorithm
round_robin(None, burst_time, arrival_time, quantum)