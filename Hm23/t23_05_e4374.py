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
    idx = 2

    for i in range(1, m + 1):
        u = int(tokens[idx])
        v = int(tokens[idx + 1])
        idx += 2
        adj[u].append((v, i))
        adj[v].append((u, i))

    k = int(tokens[idx])
    idx += 1

    removed_edge = [False] * (m + 1)

    for _ in range(k):
        c = int(tokens[idx])
        idx += 1

        current_removed = []
        for _ in range(c):
            edge_id = int(tokens[idx])
            idx += 1
            removed_edge[edge_id] = True
            current_removed.append(edge_id)

        visited = [False] * (n + 1)

        stack = [1]
        visited[1] = True
        visited_count = 1

        while stack:
            v = stack.pop()
            for to, edge_id in adj[v]:
                if not removed_edge[edge_id] and not visited[to]:
                    visited[to] = True
                    visited_count += 1
                    stack.append(to)

        if visited_count == n:
            print("Connected")
        else:
            print("Disconnected")

        for edge_id in current_removed:
            removed_edge[edge_id] = False

if __name__ == '__main__':
    main()