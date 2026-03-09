import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:]))

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        moved = False

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True

        arr[j + 1] = key

        if moved:
            print(*(arr))

if __name__ == "__main__":
    solve()