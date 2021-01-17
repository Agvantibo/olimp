#!/bin/python3

n, m, k, s = [int(i) for i in input().split()]
# n - total cities, m - total roads,
# k - number of cities w/ gas stations, s - max range
Roads = []
for i in range(m):
    Roads.append([])
    Roads[i] = [int(i) for i in input().split()]

GasStations = [int(i) for i in input().split()]
AvailableCities = [1]
NodeScan = [2 for i in range(n)]
NodeScan[0] = 1


def crawl(node, gas):
    # (0) Checking if node has been scanned twice. If it is, exit cleanly.
    if NodeScan[node - 1] <= 0:
        return 0
    else:
        NodeScan[node - 1] -= 1
    # (1) Refill gas tank if possible
    if node in GasStations:
        gas = s
    # (2) Compile a list of connections for nodes
    connections = []
    for i in Roads:
        if i[0] == node:
            connections.append([i[1], i[2]])
        elif i[1] == node:
            connections.append([i[0], i[2]])
    # (3) Check if it is possible to travel to a node.
    available_connections = []
    for i in connections:
        if i[1] <= gas:
            available_connections.append(i)
    del connections
    # (3.5) Flush available_connections to AvailableCities
    for i in available_connections:
        if i[0] not in AvailableCities:
            AvailableCities.append(i[0])
    # (4) ~Recluse!~ Recurse!
    for i in available_connections:
        crawl(i[0], gas - i[1])


crawl(1, k)
print(len(AvailableCities))
AvailableCities.sort()
print(" ".join(map(str, AvailableCities)))
