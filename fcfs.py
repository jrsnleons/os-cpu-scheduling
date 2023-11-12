from tabulate import tabulate

n = int(input("Number of processes: "))
d = dict()

for i in range(n):
    key = chr(65+i)
    at = int(input("Arrival time of " + key + ": "))
    bt = int(input("Burst time of " + key + ": "))
    d[key] = {'Arrival Time': at, 'Burst Time': bt}

# Sort the dictionary based on arrival time
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]['Arrival Time']))

# Function that gets the Finish Time
def calculate_finish_time(table):
    for key, values in table.items():
        if key == list(table.keys())[0]:
            table[key]['Finish Time'] = values['Burst Time'] + values['Arrival Time']
        else:
            table[key]['Finish Time'] = max(table[key]['Arrival Time'], table[list(table.keys())[list(table.keys()).index(key) - 1]]['Finish Time']) + table[key]['Burst Time']

# Function that gets the Turnaround Time
def calculate_turnaround_time(processes):
    sorted_processes = dict(sorted(processes.items(), key=lambda item: item[1]['Arrival Time']))

    for key, values in sorted_processes.items():
        sorted_processes[key]['Turnaround Time'] = values['Finish Time'] - values['Arrival Time']

    return sorted_processes

# Function that gets the Waiting Time
def calculate_waiting_time(processes):
    for key, values in processes.items():
        processes[key]['Waiting Time'] = values['Turnaround Time'] - values['Burst Time']

    return processes

# Calcuulate Average TaT
def calculate_turnaround_time(processes):
    total_turnaround_time = 0

    for process in processes:
        process['Turnaround Time'] = process['Finish Time'] - process['Arrival Time']
        total_turnaround_time += process['Turnaround Time']

    average_turnaround_time = total_turnaround_time / len(processes)

    return processes, avg_turnaround_time

calculate_finish_time(sorted_d)
calculate_waiting_time(sorted_d)

processes, avg_turnaround_time = calculate_turnaround_time(sorted_d)



table = []
for key, values in sorted_d.items():
    table.append([key, values['Arrival Time'], values['Burst Time'], values['Finish Time'], values['Turnaround Time'], values['Waiting Time']])
print(tabulate(table, headers=['ID', 'AT', 'BT', 'FT', 'TT', 'WT']))

print("Average TaT: {avg_turnarond_time}")