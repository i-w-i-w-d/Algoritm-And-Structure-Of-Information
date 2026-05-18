from collections import deque

def main():
    tokens = []
    try:
        while True:
            tokens.extend(input().split())
    except EOFError:
        pass

    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])

    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    idx = 2
    for _ in range(m):
        u = int(tokens[idx])
        v = int(tokens[idx + 1])
        idx += 2
        adj[u].append(v)
        in_degree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topo_order) == n:
        print(" ".join(map(str, topo_order)))
    else:
        print("-1")

if __name__ == '__main__':
    main()