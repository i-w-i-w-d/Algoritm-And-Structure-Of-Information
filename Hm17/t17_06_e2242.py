import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)

def solve():
    # Зчитуємо всі дані до символу '*'
    input_data = sys.stdin.read().split()
    chars = []

    for token in input_data:
        for ch in token:
            if ch == '*':
                break
            chars.append(ch)
        if '*' in token:
            break

    if not chars:
        print()
        return

    reversed_chars = chars[::-1]

    root = None
    for ch in reversed_chars:
        root = insert(root, ch)

    result = []
    preorder(root, result)
    print("".join(result))

if __name__ == '__main__':
    solve()