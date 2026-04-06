import sys

def is_balanced(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

line = sys.stdin.read().strip()
if is_balanced(line):
    print("yes")
else:
    print("no")