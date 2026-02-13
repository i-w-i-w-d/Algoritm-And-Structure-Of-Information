from bisect import bisect_left, bisect_right

try:
    line1 = input()
    if not line1:
        exit()
    n = int(line1)

    mutants = list(map(int, input().split()))

    m = int(input())

    queries = list(map(int, input().split()))

    for color in queries:
        count = bisect_right(mutants, color) - bisect_left(mutants, color)
        print(count)
except EOFError:
    pass