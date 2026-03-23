import sys
sys.set_int_max_str_digits(100000)
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = divmod(x, 10 ** m)
    high2, low2 = divmod(y, 10 ** m)

    z2 = karatsuba(high1, high2)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(high1 + low1, high2 + low2) - z2 - z0

    return (z2 * 10 ** (2 * m)) + (z1 * 10 ** m) + z0

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    num1 = int(input_data[0])
    num2 = int(input_data[1])

    print(karatsuba(num1, num2))

if __name__ == "__main__":
    main()