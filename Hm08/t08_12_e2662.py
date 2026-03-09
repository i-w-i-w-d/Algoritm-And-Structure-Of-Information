import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:]))

    target_val = arr[0]
    target_moves = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            if arr[i] == target_val or arr[min_idx] == target_val:
                target_moves += 1

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(target_moves)

if __name__ == "__main__":
    solve()