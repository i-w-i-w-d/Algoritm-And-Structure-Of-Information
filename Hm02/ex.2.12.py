def task_2_12(n):
    # h(n) = f(n) + g(n)
    # Якщо брати оптимізовані версії: O(1) + O(n) = O(n)
    part_f = n * (n + 1) // 2

    part_g = 0
    for i in range(1, n + 1):
        part_g += i + (i * (i + 1) // 2)

    return part_f + part_g