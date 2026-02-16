def f_poly(x):
    return x ** 3 + 4 * x ** 2 + x - 6

def solve_45():
    left = 0.0
    right = 2.0

    for _ in range(100):
        mid = (left + right) / 2
        if f_poly(mid) < 0:
            left = mid
        else:
            right = mid

    print(f"\nКорінь x^3 + 4x^2 + x - 6 = 0: {right:.10f}")

solve_45()