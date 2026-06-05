import math

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

    while True:
        try:
            n_str = next(tokens)
        except StopIteration:
            break

        n = int(n_str)
        if n == 0:
            break

        coords = []
        for _ in range(n):
            x = int(next(tokens))
            y = int(next(tokens))
            coords.append((x, y))

        min_dist = [float('inf')] * n
        min_dist[0] = 0.0
        visited = [False] * n
        total_cost = 0.0

        for _ in range(n):
            u = -1
            best_dist = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < best_dist:
                    best_dist = min_dist[i]
                    u = i

            visited[u] = True
            total_cost += best_dist

            x1, y1 = coords[u]

            for v in range(n):
                if not visited[v]:
                    x2, y2 = coords[v]
                    dx = x1 - x2
                    dy = y1 - y2
                    dist = math.sqrt(dx * dx + dy * dy)

                    if dist < min_dist[v]:
                        min_dist[v] = dist

        print(f"{total_cost:.2f}")

solve()