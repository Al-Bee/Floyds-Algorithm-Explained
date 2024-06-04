import math

def floyd(dg):
    d = [*dg]
    for x in range(len(dg)):
        for u in range(len(dg)):
            for v in range(len(dg)):
                print(f"Current intermediate (x) node: {x}")
                print(f"Current source (u) node: {u}")
                print(f"Current target (v) node: {v}")
                print(f"Direct path (u -> v) cost: {d[u][v]}")
                print(f"Intermediate path cost: (u -> x) {u} -> {x} (cost: {d[u][x]}) + (x -> v) {x} -> {v} (cost: {d[x][v]}) = {d[u][x] + d[x][v]}")
                print(f"direct cost > intermediate cost: {d[u][v] > (d[u][x] + d[x][v])}\n")
                d[u][v] = min(d[u][v], (d[u][x] + d[x][v]))
    return d

dg = [[0, 3, math.inf, 7], [8, 0, 2, math.inf], [5, math.inf, 0, 1], [2, math.inf, math.inf, 0]]
for i in dg:
    print(i)
print()
apsp = floyd(dg)
for i in apsp:
    print(i)
