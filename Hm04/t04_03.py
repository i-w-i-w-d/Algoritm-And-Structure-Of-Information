def f(x):
    return x ** 2 + x + 1

def solve_43():
    left = 0.0
    right = 10.0

    for _ in range(100):
        mid = (left + right) / 2
        if f(mid) < 5:
            left = mid
        else:
            right = mid

    print(f"\nНайменше x: {right:.10f}")

solve_43()