def task_2_10(n):
    # Асимптотична оцінка: O(n)
    # Найгірший випадок: виконується n ітерацій
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

def task_2_10_optimized(n):
    # Асимптотична оцінка: O(1)
    # Використання формули арифметичної прогресії
    return n * (n + 1) // 2