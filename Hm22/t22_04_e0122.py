import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)

    try:
        n = int(next(it))
        k = int(next(it))
        start = int(next(it))
        end = int(next(it))
        max_d = int(next(it))

        adj = [[] for _ in range(n + 1)]
        for _ in range(k):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)

    except StopIteration:
        pass

    visited = [False] * (n + 1)
    total_paths = 0

    def dfs(u, current_dist):
        nonlocal total_paths

        if u == end and current_dist > 0:
            total_paths += 1

        if current_dist >= max_d:
            return

        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v, current_dist + 1)
        visited[u] = False

    dfs(start, 0)
    print(total_paths)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    solve()