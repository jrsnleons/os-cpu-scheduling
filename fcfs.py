from tabulate import tabulate

n = int(input("Number of processes: "))
d = dict()

for i in range(n):
    key = chr(65+i)
    at = int(input("Arrival time of " + key + ": "))
    bt = int(input("Burst time of " + key + ": "))
    d[key] = {'Arrival Time': at, 'Burst Time': bt}

# Display the sorted data using tabulate
table = []
for key, values in sorted(d.items()):
    table.append([key, values['Arrival Time'], values['Burst Time']])

print(tabulate(table, headers=['ID', 'AT', 'BT']))

# Sort the dictionary based on arrival time
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]['Arrival Time']))

# Function that gets the Finish Time
def ft(table):
    for n in table:
        if n == 0:
            table["ft"] = table[n][2] + table[n][1]
        else:
            table["ft"] = table[n-1][3] + table[n][2]


ft(sorted_d)

print("/n")
table2 = []
for key, values in sorted(d.items()):
    table2.append([key, values['AT'], values['BT'], values['FT']])

print(tabulate(table, headers=['ID', 'AT', 'BT', 'FT']))


