from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    half = n // 2

    q1 = deque(int(x) for x in input_data[1: half + 1])
    q2 = deque(int(x) for x in input_data[half + 1: n + 1])

    moves = 0
    limit = 200000

    while q1 and q2 and moves < limit:
        c1 = q1.popleft()
        c2 = q2.popleft()

        if c1 == 0 and c2 == n - 1:
            q1.append(c1)
            q1.append(c2)
        elif c2 == 0 and c1 == n - 1:
            q2.append(c1)
            q2.append(c2)
        elif c1 > c2:
            q1.append(c1)
            q1.append(c2)
        else:
            q2.append(c1)
            q2.append(c2)

        moves += 1

    if not q1:
        print(f"second {moves}")
    elif not q2:
        print(f"first {moves}")
    else:
        print("draw")

if __name__ == "__main__":
    solve()