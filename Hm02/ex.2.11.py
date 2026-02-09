def task_2_11(n):
    # Асимптотична оцінка: O(n ^ 2)
    # Зовнішній цикл виконується n разів.
    # Внутрішній виклик (sum від 1 до i) виконується i разів.
    result = 0
    for i in range(1, n + 1):
        # Імітація виклику неоптимізованої функції f(i)
        term = 0
        for j in range(1, i + 1):
            term += j
        result += i + term
    return result

def task_2_11_optimized(n):
    # Асимптотична оцінка: O(n)
    result = 0
    for i in range(1, n + 1):
        # (i * (i + 1) // 2) виконується за O(1)
        result += i + (i * (i + 1) // 2)
    return result