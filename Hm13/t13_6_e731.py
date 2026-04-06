import sys

def solve():
    data = sys.stdin.read().strip()
    if not data:
        return

    stack = []
    operators = {'+', '-', '*', '/'}

    for char in reversed(data):
        if char not in operators:
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_expr = f"({op1}{char}{op2})"
            stack.append(new_expr)

    if stack:
        print(stack.pop())

if __name__ == "__main__":
    solve()