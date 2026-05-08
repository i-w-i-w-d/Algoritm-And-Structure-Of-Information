import sys
input_data = sys.stdin.read().split()

if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
edges = set()
has_multi = False
idx = 2

for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    idx += 2
    pair = (u, v)
    if pair in edges:
        has_multi = True
    else:
        edges.add(pair)

if has_multi:
    print("YES")
else:
    print("NO")