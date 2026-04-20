import sys

sys.setrecursionlimit(200005)

class Employee:
    def __init__(self, id, fee):
        self.id = id
        self.fee = fee
        self.subordinates = []
        self.min_cost = 0

def solve(emp):
    if not emp.subordinates:
        emp.min_cost = emp.fee
        return

    min_sub = -1
    for sub in emp.subordinates:
        solve(sub)
        if min_sub == -1 or sub.min_cost < min_sub:
            min_sub = sub.min_cost

    emp.min_cost = emp.fee + min_sub

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    emps = [None] * (n + 1)
    sub_ids = [[] for _ in range(n + 1)]

    idx = 1
    for i in range(1, n + 1):
        fee = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        emps[i] = Employee(i, fee)
        for _ in range(k):
            sub_ids[i].append(int(input_data[idx]))
            idx += 1

    for i in range(1, n + 1):
        for sub_id in sub_ids[i]:
            emps[i].subordinates.append(emps[sub_id])

    if emps[1]:
        solve(emps[1])
        print(emps[1].min_cost)

if __name__ == '__main__':
    main()