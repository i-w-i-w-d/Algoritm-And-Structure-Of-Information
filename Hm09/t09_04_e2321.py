import sys
import random

sys.setrecursionlimit(2000)

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = random.randint(low, high)
        arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    if n > 1:
        quick_sort(arr, 0, n - 1)

    print(*(arr))

if __name__ == '__main__':
    main()