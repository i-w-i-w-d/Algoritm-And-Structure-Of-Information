import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    n = int(input_data[1])

    grid = input_data[2:m + 2]
    visited = [[False] * n for _ in range(m)]
    components = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                components += 1

                st = [(i, j)]
                visited[i][j] = True

                while st:
                    r, c = st.pop()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            if grid[nr][nc] == '#' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                st.append((nr, nc))
    print(components)

if __name__ == '__main__':
    solve()