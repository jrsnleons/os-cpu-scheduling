
n = int(input("Number of processes: "))
d = dict()

for i in range(n):
    key = chr(65+i)
    at = int(input("Arrival time of " + key + ": "))
    bt = int(input("Burst time of " + key + ": ")) 
    l = []
    l.append(at)
    l.append(bt)
    d[key] = l

d = sorted(d.items(), key=lambda item: item[1][0])
