import sys

sys.setrecursionlimit(200000)

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
    else:
        root.right = insert(root.right, val)
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    return (p.val == q.val) and \
        is_same_tree(p.left, q.left) and \
        is_same_tree(p.right, q.right)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    data = list(map(int, input_data))

    n1 = data[0]
    arr1 = data[1: n1 + 1]

    if n1 + 1 < len(data):
        n2 = data[n1 + 1]
        arr2 = data[n1 + 2: n1 + 2 + n2]
    else:
        arr2 = []

    root1 = None
    for val in arr1:
        root1 = insert(root1, val)

    root2 = None
    for val in arr2:
        root2 = insert(root2, val)

    if is_same_tree(root1, root2):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    solve()