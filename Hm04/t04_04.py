import math

def solve_44():
    left = 1.6
    right = 3.0

    for _ in range(100):
        mid = (left + right) / 2
        if math.sin(mid) - mid / 3 > 0:
            left = mid
        else:
            right = mid

    print(f"\nКорінь sin(x)=x/3: {right:.10f}")

solve_44()