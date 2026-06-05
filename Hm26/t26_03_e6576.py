import heapq

def solve():
    def get_tokens():
        try:
            while True:
                line = input().split()
                for token in line:
                    yield token
        except EOFError:
            pass

    tokens = get_tokens()

    try:
        t = int(next(tokens))
    except StopIteration:
        return

    for _ in range(t):
        n = int(next(tokens))
        m = int(next(tokens))
        p = int(next(tokens))
        q = int(next(tokens))

        adj = [[] for _ in range(n + 1)]

        for _ in range(m):
            u = int(next(tokens))
            v = int(next(tokens))
            w = int(next(tokens))
            adj[u].append((w, v))
            adj[v].append((w, u))

        visited = [False] * (n + 1)
        min_heap = [(0, 1, -1)]

        is_in_mst = False
        nodes_count = 0

        while min_heap and nodes_count < n:
            w, u, parent = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            nodes_count += 1

            if (u == p and parent == q) or (u == q and parent == p):
                is_in_mst = True
                break

            for weight, v in adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v, u))

        if is_in_mst:
            print("YES")
        else:
            print("NO")

solve()