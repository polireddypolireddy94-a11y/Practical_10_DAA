
n = 4
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

edges.sort()
parent = list(range(n))
cost = 0

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, ":", w)
        cost += w
        parent[a] = b

print("Minimum Cost:", cost)
