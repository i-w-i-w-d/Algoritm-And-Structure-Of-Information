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
    s = int(data[1]) - 1
    f = int(data[2]) - 1

    matrix = []
    idx = 3
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(data[idx]))
            idx += 1
        matrix.append(row)

    dist = [float('inf')] * n
    dist[s] = 0
    visited = [False] * n

    for _ in range(n):
        min_d = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i

        if u == -1 or u == f:
            break

        visited[u] = True

        for v in range(n):
            w = matrix[u][v]
            if w != -1 and not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    if dist[f] == float('inf'):
        print(-1)
    else:
        print(dist[f])

if __name__ == '__main__':
    solve()