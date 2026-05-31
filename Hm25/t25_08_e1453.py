def solve():
    data = []
    try:
        while True:
            data.extend(input().split())
    except EOFError:
        pass

    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        edges.append((u, v, w))
        idx += 3

    dist = [float('inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    ans = []
    for d in dist:
        if d == float('inf'):
            ans.append(30000)
        else:
            ans.append(d)

    print(*(ans))

if __name__ == '__main__':
    solve()