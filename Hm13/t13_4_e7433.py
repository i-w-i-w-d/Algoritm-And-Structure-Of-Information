import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    k = int(input_data[1])

    if n == 0:
        print(0)
        return

    stack = []
    while n > 0:
        remainder = n % k
        if remainder > 9:
            stack.append(f"[{remainder}]")
        else:
            stack.append(str(remainder))
        n //= k
    print("".join(stack[::-1]))

solve()