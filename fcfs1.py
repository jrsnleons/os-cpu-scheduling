from tabulate import tabulate

def calculate_turnaround_time(processes):
    total_turnaround_time = 0

    for process in processes:
        process['tat'] = process['ft'] - process['at']
        total_turnaround_time += process['tat']

    average_turnaround_time = total_turnaround_time / len(processes)

    return processes, average_turnaround_time

def calculate_waiting_time(processes):
    total_waitiing_time = 0
    for process in processes:
        process['wt'] = process['tat'] - process['bt']
        total_waitiing_time += process['wt']
        
    average_waiting_time = total_waitiing_time / len(processes)

    return processes, average_waiting_time

def print_timeline(processes):
    sorted_processes = sorted(processes, key=lambda x: x['at'])
    print("\nTimeline: ")
    print("|  ", end="")
    for process in sorted_processes:
        print(process['pid'] + "  |  ", end="")

    
    for index, process in enumerate(sorted_processes):
        if index == 0:
            print("\n"+ str(process['at']), end="     ")
            print(process['ft'], end="     ")
        else:
            print(process['ft'], end="")
            if len(str(process['ft'])) > 1:
                print("    ", end="")
            else:
                print("     ", end="")


def print_table(processes):
    sorted_processes = sorted(processes, key=lambda x: x['at'])
    table = []
    for process in processes:
        table.append([process['pid'], process['at'], process['bt'], process['ft'], process['tat'], process['wt']])
    print(tabulate(table, headers=['PID', 'AT', 'BT', 'FT', 'TaT', 'WT']))


def calculate_ft(processes):
    previous_finish_time = 0
    sorted_processes = sorted(processes, key=lambda x: x['at']) 
    print(sorted_processes)
    for i, process in enumerate(sorted_processes):
        if i == 0:
            if process['at'] == 0:
                process['ft'] = process['bt']
            else:
                process['ft'] = process['bt'] + process['at']
        else:
            process['ft'] = previous_finish_time + process['bt']#prev proces ft + bt
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
    proessess = calculate_ft(processes)


    # Calculate turnaround time
    processes, avg_tat = calculate_turnaround_time(processes)

    # Calculate waiting time
    processes, avg_wt = calculate_waiting_time(processes)

    # Format to 2 decmals
    avg_tat = "{:.2f}".format(avg_tat)
    avg_wt = "{:.2f}".format(avg_wt)

        
    # Display the data using tabulate
    print_table(processes)
    
    # Display Averages
    print(f"\nAverage Turnaround Time: {avg_tat}")
    print(f"\nAverage Waiting Time: {avg_wt}")

    # Display Timeline
    print_timeline(processes)

if __name__ == "__main__":
    main()
