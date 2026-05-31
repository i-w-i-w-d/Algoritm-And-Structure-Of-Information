def solve():
    data = []
    try:
        while True:
            data.extend(input().split())
    except EOFError:
        pass

    if not data:
        return

    n = int(data[0])
    idx = 1

    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(data[idx]))
            idx += 1
        matrix.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    for row in matrix:
        print(*(row))

if __name__ == '__main__':
    solve()