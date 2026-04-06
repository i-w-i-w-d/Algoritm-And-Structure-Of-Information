import sys

def solve():
    expr = sys.stdin.read().strip()
    if not expr:
        return

    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []

    for char in reversed(expr):
        if char not in prec:
            stack.append((char, 9))
        else:
            op1_val, op1_prec = stack.pop()
            op2_val, op2_prec = stack.pop()

            curr_prec = prec[char]

            if op1_prec < curr_prec:
                op1_val = f"({op1_val})"

            if op2_prec < curr_prec or (op2_prec == curr_prec and char in '-/'):
                op2_val = f"({op2_val})"

            new_expr = f"{op1_val}{char}{op2_val}"
            stack.append((new_expr, curr_prec))

    if stack:
        print(stack.pop()[0])

if __name__ == "__main__":
    solve()