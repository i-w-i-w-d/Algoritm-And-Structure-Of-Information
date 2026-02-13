import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx])
    idx += 1

    collection = set(input_data[idx: idx + n])
    idx += n

    m = int(input_data[idx])
    idx += 1

    queries = input_data[idx: idx + m]

    results = []
    for k in queries:
        if k in collection:
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()