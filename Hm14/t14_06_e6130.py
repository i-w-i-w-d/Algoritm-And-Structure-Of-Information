import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, n):
        new_node = Node(n)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        return "ok"

    def push_back(self, n):
        new_node = Node(n)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if not self.head:
            return "error"
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_back(self):
        if not self.tail:
            return "error"
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def front(self):
        if not self.head:
            return "error"
        return self.head.data

    def back(self):
        if not self.tail:
            return "error"
        return self.tail.data

    def size(self):
        return self._size

    def clear(self):
        self.head = self.tail = None
        self._size = 0
        return "ok"

def main():
    d = Deque()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        cmd = parts[0]
        if cmd == "push_front":
            print(d.push_front(int(parts[1])))
        elif cmd == "push_back":
            print(d.push_back(int(parts[1])))
        elif cmd == "pop_front":
            print(d.pop_front())
        elif cmd == "pop_back":
            print(d.pop_back())
        elif cmd == "front":
            print(d.front())
        elif cmd == "back":
            print(d.back())
        elif cmd == "size":
            print(d.size())
        elif cmd == "clear":
            print(d.clear())
        elif cmd == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()