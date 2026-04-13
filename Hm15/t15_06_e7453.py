import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def rotate_right(self, k):
        if self.count <= 1:
            return

        k = k % self.count
        if k == 0:
            return

        steps_to_new_tail = self.count - k

        self.tail.next = self.head

        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        self.tail = new_tail
        self.tail.next = None

    def display(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.data))
            current = current.next
        print(" ".join(res))

def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word

    input_gen = get_input()

    try:
        n = int(next(input_gen))

        lst = LinkedList()
        for _ in range(n):
            lst.append(int(next(input_gen)))

        for k_str in input_gen:
            k = int(k_str)
            lst.rotate_right(k)
            lst.display()

    except StopIteration:
        pass

if __name__ == "__main__":
    solve()