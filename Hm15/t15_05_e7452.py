import sys

sys.setrecursionlimit(2000)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_direct(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

    def print_reverse(self):
        elements = []
        self._recursive_collect(self.head, elements)
        print(" ".join(elements))

    def _recursive_collect(self, node, acc):
        if node is None:
            return
        self._recursive_collect(node.next, acc)
        acc.append(str(node.data))

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    lst = LinkedList()

    for i in range(1, n + 1):
        lst.append(int(input_data[i]))

    lst.print_direct()
    lst.print_reverse()

if __name__ == "__main__":
    solve()