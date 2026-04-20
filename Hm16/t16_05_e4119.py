import sys

sys.setrecursionlimit(200005)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

def insert(root, parts):
    curr = root
    for part in parts:
        if part not in curr.children:
            curr.children[part] = Node(part)
        curr = curr.children[part]

def print_tree(node, depth):
    for name in sorted(node.children.keys()):
        sys.stdout.write(" " * depth + name + "\n")
        print_tree(node.children[name], depth + 1)

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0].strip())
    root = Node("")

    for i in range(1, n + 1):
        if i < len(lines):
            path = lines[i].strip()
            if path:
                parts = path.split('\\')
                insert(root, parts)

    print_tree(root, 0)

if __name__ == '__main__':
    main()