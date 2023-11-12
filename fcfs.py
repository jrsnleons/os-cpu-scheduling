from tabulate import tabulate

def calculate_turnaround_time(processes):
    total_turnaround_time = 0

    for process in processes:
        process['tat'] = process['ft'] - process['at']
        total_turnaround_time += process['tat']

    average_turnaround_time = total_turnaround_time / len(processes)

    return processes, average_turnaround_time

def calculate_waiting_time(processes):
    total_waiting_time = 0
    for process in processes:
        process['wt'] = process['tat'] - process['bt']
        total_waiting_time += process['wt']
        
    average_waiting_time = total_waiting_time / len(processes)

    return processes, average_waiting_time

def calculate_cpu_utilization(processes):
    total_burst_time = sum(process['bt'] for process in processes)
    total_turnaround_time = sum(process['tat'] for process in processes)
    
    cpu_utilization = (total_burst_time / total_turnaround_time) * 100
    return cpu_utilization

def print_timeline(processes):
    sorted_processes = sorted(processes, key=lambda x: x['at'])
    
    timeline = []
    for process in sorted_processes:
        timeline.extend([process['pid']] * process['bt'])
    
    print("\nGantt Chart:")
    for task in timeline:
        print(f"{task:^4}", end="")
    print()
    for i in range(len(timeline)):
        print(f"{i + 1:^4}", end="")
    print()

def print_table(processes):
    sorted_processes = sorted(processes, key=lambda x: x['at'])
    table = []
    for process in processes:
        table.append([process['pid'], process['at'], process['bt'], process['ft'], process['tat'], process['wt']])
    print(tabulate(table, headers=['PID', 'AT', 'BT', 'FT', 'TaT', 'WT']))

def calculate_ft(processes):
    previous_finish_time = 0
    sorted_processes = sorted(processes, key=lambda x: x['at'])
    for i, process in enumerate(sorted_processes):
        if i == 0:
            if process['at'] == 0:
                process['ft'] = process['bt']
            else:
                process['ft'] = process['bt'] + process['at']
        else:
            process['ft'] = previous_finish_time + process['bt']
        previous_finish_time = process['ft']
    return sorted_processes

def main():
    # n = int(input("Number of processes: "))
    # processes = []

    # User input on processes
    # for i in range(n):
    #     process_id = chr(65 + i)
    #     arrival_time = int(input(f"Arrival time of Process {process_id}: "))
    #     burst_time = int(input(f"Burst time of Process {process_id}: "))
    #     processes.append({'pid': process_id, 'at': arrival_time, 'bt': burst_time, 'ft': 0, 'tat': 0, 'wt': 0})

    # dummy data
    n = 3
    processes = [{'pid': 'A', 'at': 5, 'bt': 7, 'ft': 0, 'tat': 0, 'wt': 0}, {'pid': 'B', 'at': 2, 'bt': 5, 'ft': 0, 'tat': 0, 'wt': 0}, {'pid': 'C', 'at': 8, 'bt': 2, 'ft': 0, 'tat': 0, 'wt': 0}]

    # Calculate finish time
    processes = calculate_ft(processes)

    # Calculate turnaround time
    processes, avg_tat = calculate_turnaround_time(processes)

    # Calculate waiting time
    processes, avg_wt = calculate_waiting_time(processes)

    # Calculate CPU utilization
    cpu_utilization = calculate_cpu_utilization(processes)

    # Format to 2 decimals
    avg_tat = "{:.2f}".format(avg_tat)
    avg_wt = "{:.2f}".format(avg_wt)

    # Display the Gantt chart
    print_timeline(processes)

    # Display the data using tabulate
    print_table(processes)
    
    # Display Averages and CPU Utilization
    print(f"\nAverage Turnaround Time: {avg_tat}")
    print(f"Average Waiting Time: {avg_wt}")
    print(f"CPU Utilization: {cpu_utilization:.2f}%")

if __name__ == "__main__":
    main()
