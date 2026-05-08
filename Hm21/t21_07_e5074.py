n, m = map(int, input().split())
degrees = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

for i in range(1, n + 1):
    print(degrees[i])