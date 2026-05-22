import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    grid = [list(row) for row in input_data[1:n + 1]]

    start = None
    target = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                target = (i, j)

    q = deque([start])
    visited = {start: None}
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False

    while q:
        r, c = q.popleft()
        if (r, c) == target:
            found = True
            break

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] in ('.', 'X') and (nr, nc) not in visited:
                    visited[(nr, nc)] = (r, c)
                    q.append((nr, nc))

    if found:
        print("Y")
        curr = target
        while curr != start:
            grid[curr[0]][curr[1]] = '+'
            curr = visited[curr]
        for row in grid:
            print("".join(row))
    else:
        print("N")

if __name__ == '__main__':
    solve()