#!/bin/python3

n, m, k, s = [int(i) for i in input().split()]
# n - total cities, m - total roads, 
# k - number of cities w/ gas stations, s - max range
Roads = []
for i in range(m):
    Roads.append([])
    Roads[i] = [int(i) for i in input().split()]

GasStations = [int(i) for i in input().split()]
AvailableCities = []
NodeScan = [2 for i in range(n)]
NodeScan[0] = 1

def Crawl(Node, Gas):
    # (0) Checking if node has been scanned twice. If it is, exit cleanly.
    if NodeScan[Node - 1] <= 0:
        return 0
    else:
        NodeScan[Node - 1] -= 1
    # (1) Refill gas tank if possible
    if Node in GasStations:
        Gas = s
    # (2) Compile a list of connections for nodes
    Connections = []
    for i in Roads:
        if i[0] == Node:
            Connections.append([i[1], i[2]])
        elif i[1] == Node:
            Connections.append([i[0], i[2]])
    # (3) Check if it is possible to travel to a node.
    AvailableConnections = []
    for i in Connections:
        if i[1] <= Gas:
            AvailableConnections.append(i)
    del Connections
    # (3.5) Flush AvailableConnections to AvailableCities
    for i in AvailableConnections:
        if i[0] not in AvailableCities:
            AvailableCities.append(i[0])
    # (4) ~Recluse!~ Recurse!
    for i in AvailableConnections:
        Crawl(i[0], Gas - i[1])


Crawl(1, k)
print(len(AvailableCities))
AvailableCities.sort()
print(" ".join(map(str, AvailableCities)))
