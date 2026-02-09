#a) Сума i від 0 до n. Оцінка часу: O(n)
def task_2_14_a(n):
    total = 0
    #Цикл виконується n + 1 разів -> O(n)
    for i in range(n + 1):
        total += i
    return total


#b) Сума i ^ 2 від 0 до n. Оцінка часу: O(n)
def task_2_14_b(n):
    total = 0
    #Цикл виконується n+1 разів -> O(n)
    #Множення i * i -> O(1)
    for i in range(n + 1):
        total += i * i
    return total


#c) Сума a^i від 0 до n. Оцінка часу: O(n)
def task_2_14_c(n, a=2):
    total = 0
    current_pow = 1  # a^0

    #Цикл виконується n + 1 разів -> O(n)
    for i in range(n + 1):
        total += current_pow
        #O(1)
        current_pow *= a
    return total


#d) Сума i ^ i від 0 до n. Оцінка часу: O(n^2)
def task_2_14_d(n):
    total = 0
    #Зовнішній цикл -> n разів
    for i in range(n + 1):

        #Обчислення i ^ i через цикл
        #Внутрішній цикл виконується i разів
        #O(n^2)
        term = 1
        for j in range(i):
            term *= i

        total += term
    return total


#e) Добуток 1 / (1 + i) від 1 до n. Оцінка часу: O(n)
def task_2_14_e(n):
    product = 1.0
    #Цикл виконується n разів -> O(n)
    for i in range(1, n + 1):
        product *= (1.0 / (1 + i))
    return product


#f)Добуток 1 / (1 + i!) від 1 до n. Оцінка часу: O(n)
def task_2_14_f(n):
    product = 1.0
    current_fact = 1

    #Цикл виконується n разів -> O(n)
    for i in range(1, n + 1):
        #i! = (i - 1)! * i. Операція O(1).
        current_fact *= i

        product *= (1.0 / (1 + current_fact))
    return product


#g) Добуток a ^ i / (1 + i!) від 1 до n. Оцінка часу: O(n)
def task_2_14_g(n, a=2):
    product = 1.0
    current_pow = 1  #Зберігає a ^ i
    current_fact = 1  #Зберігає i!

    #Цикл виконується n разів -> O(n)
    for i in range(1, n + 1):
        current_pow *= a  #O(1)
        current_fact *= i  #O(1)

        product *= (current_pow / (1 + current_fact))
    return product


#h) Добуток 1 / (1 + i ^ m) від 1 до n. Оцінка часу: O(nm)
def task_2_14_h(n, m = 3):
    product = 1.0

    #Зовнішній цикл: n разів
    for i in range(1, n + 1):
        #Обчислення i ^ m через цикл
        #Внутрішній цикл виконується m разів
        #n * m -> O(nm)
        pow_val = 1
        for k in range(m):
            pow_val *= i

        product *= (1.0 / (1 + pow_val))
    return product


#i) Добуток 1 / (1 + i ^ i) від 1 до n. Оцінка часу: O(n ^ 2)
def task_2_14_i(n):
    product = 1.0

    #Зовнішній цикл: n разів
    for i in range(1, n + 1):

        #Внутрішній цикл виконується i разів
        #Сумарна кількість ітерацій = n ^ 2 / 2 -> O(n ^ 2)
        pow_val = 1
        for j in range(i):
            pow_val *= i

        product *= (1.0 / (1 + pow_val))
    return product