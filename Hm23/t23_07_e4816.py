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
    for _ in range(m):
        u = int(tokens[idx])
        v = int(tokens[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            comp = []

            stack = [i]
            visited[i] = True

            while stack:
                v = stack.pop()
                comp.append(v)
                for to in adj[v]:
                    if not visited[to]:
                        visited[to] = True
                        stack.append(to)

            components.append(comp)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))

if __name__ == '__main__':
    main()