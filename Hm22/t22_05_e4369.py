import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx]);
    idx += 1
    m = int(input_data[idx]);
    idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]);
        idx += 1
        v = int(input_data[idx]);
        idx += 1
        adj[u].append(v)
        adj[v].append(u)

    num_sources = int(input_data[idx]);
    idx += 1
    dist = [-1] * (n + 1)
    queue = deque()

    for _ in range(num_sources):
        s = int(input_data[idx]);
        idx += 1
        dist[s] = 0
        queue.append(s)

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    max_dist = 0
    last_node = 1

    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            last_node = i
        elif dist[i] == max_dist:
            if last_node == 0 or i < last_node:
                last_node = i

    print(max_dist)
    print(last_node)

if __name__ == "__main__":
    solve()