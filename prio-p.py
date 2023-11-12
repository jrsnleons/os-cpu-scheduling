from tabulate import tabulate

def priority_preemptive(processes, burst_time, arrival_time, priority):
    n = len(processes)
    
    # Convert process names to letters A, B, C, ...
    process_names = [chr(65 + i) for i in range(n)]
    
    # Initialize waiting time and turnaround time arrays
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Initialize remaining time for each process
    remaining_time = burst_time.copy()
    
    # Initialize the time variable to keep track of current time
    time = 0
    
    # Initialize Gantt chart string
    gantt_chart = ""
    gantt_chart_numbers = ""
    
    # Continue processing until all processes are done
    while any(remaining_time):
        min_priority = float('inf')
        selected_process = None

        for i in range(n):
            if remaining_time[i] > 0 and arrival_time[i] <= time and priority[i] < min_priority:
                min_priority = priority[i]
                selected_process = i

        if selected_process is not None:
            gantt_chart += f"{process_names[selected_process]:^3}"
            gantt_chart_numbers += f"{time:^3}"
            remaining_time[selected_process] -= 1

            if remaining_time[selected_process] == 0:
                turnaround_time[selected_process] = time + 1 - arrival_time[selected_process]
                waiting_time[selected_process] = turnaround_time[selected_process] - burst_time[selected_process]
                
        time += 1
    
    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    
    # Create a table for input and output data
    table_data = list(zip(process_names, burst_time, arrival_time, priority, waiting_time, turnaround_time))
    headers = ["Process", "Burst Time", "Arrival Time", "Priority", "Waiting Time", "Turnaround Time"]
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
processes = input("Enter process names (separated by space): ").split()
burst_time = list(map(int, input("Enter burst times (separated by space): ").split()))
arrival_time = list(map(int, input("Enter arrival times (separated by space): ").split()))
priority = list(map(int, input("Enter priorities (separated by space): ").split()))

# Run the Priority Preemptive algorithm
priority_preemptive(processes, burst_time, arrival_time, priority)
