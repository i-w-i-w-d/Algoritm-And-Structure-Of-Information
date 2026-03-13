import sys


def merge_sort(arr, temp_arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, temp_arr, left, mid)
        merge_sort(arr, temp_arr, mid + 1, right)

        merge(arr, temp_arr, left, mid, right)


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i][0] <= arr[j][0]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp_arr[idx]


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    robots = []
    idx = 1
    for _ in range(n):
        robots.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2

    temp_arr = [None] * n
    merge_sort(robots, temp_arr, 0, n - 1)

    out = [f"{r[0]} {r[1]}" for r in robots]
    print('\n'.join(out))


if __name__ == '__main__':
    main()