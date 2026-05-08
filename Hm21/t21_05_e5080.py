n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

hanging_vertices = 0

for row in matrix:
    count = 0
    for val in row:
        if val == 1:
            count += 1

    if count == 1:
        hanging_vertices += 1

print(hanging_vertices)