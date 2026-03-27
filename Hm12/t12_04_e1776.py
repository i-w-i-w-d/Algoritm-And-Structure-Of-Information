import sys

def can_rearrange(n, target):
    stack = []
    current_car = 1
    for car in target:
        while current_car <= n and (not stack or stack[-1] != car):
            stack.append(current_car)
            current_car += 1

        if stack and stack[-1] == car:
            stack.pop()
        else:
            return False
    return True

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break

        while True:
            first_val = int(input_data[idx])
            if first_val == 0:
                idx += 1
                print()
                break

            target = [first_val]
            for _ in range(n - 1):
                idx += 1
                target.append(int(input_data[idx]))
            idx += 1

            if can_rearrange(n, target):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    solve()