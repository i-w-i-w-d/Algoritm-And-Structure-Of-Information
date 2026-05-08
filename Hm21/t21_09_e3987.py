n, m = map(int, input().split())
expected_edges = n * (n - 1) // 2
edges = set()
has_loop = False

for i in range(m):
    u, v = map(int, input().split())
    if u == v:
        has_loop = True
    if u > v:
        u, v = v, u
    edges.add((u, v))

if not has_loop and len(edges) == expected_edges:
    print("YES")
else:
    print("NO")