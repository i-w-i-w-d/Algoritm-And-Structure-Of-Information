import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input_data[i])

    for i in range(1, n // 2 + 1):
        left_child = 2 * i
        right_child = 2 * i + 1

        if left_child <= n and a[i] > a[left_child]:
            print("NO")
            return
        if right_child <= n and a[i] > a[right_child]:
            print("NO")
            return

    print("YES")

if __name__ == '__main__':
    main()