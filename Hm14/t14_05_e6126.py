import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, n):
        new_node = Node(n)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self._size += 1
        return "ok"

    def pop(self):
        if not self.head:
            return "error"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return val

    def front(self):
        if not self.head:
            return "error"
        return self.head.data

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

def main():
    q = Queue()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        cmd = parts[0]
        if cmd == "push":
            print(q.push(int(parts[1])))
        elif cmd == "pop":
            print(q.pop())
        elif cmd == "front":
            print(q.front())
        elif cmd == "size":
            print(q.size())
        elif cmd == "clear":
            print(q.clear())
        elif cmd == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()