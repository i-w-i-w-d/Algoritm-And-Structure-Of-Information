import math

def solve_42():
    try:
        line = input().strip()
        if not line: return
        c = float(line)
        left = 0.0
        right = 10 ** 10

        for _ in range(100):
            mid = (left + right) / 2
            if mid ** 2 + math.sqrt(mid) < c:
                left = mid
            else:
                right = mid

        print(f"{right:.10f}")
    except EOFError:
        pass

if __name__ == "__main__":
    solve_42()