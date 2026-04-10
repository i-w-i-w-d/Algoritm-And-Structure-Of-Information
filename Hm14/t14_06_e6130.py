import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0

    def push_front(self, n):
        node = Node(n)
        if not self.head: self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1
        return "ok"

    def push_back(self, n):
        node = Node(n)
        if not self.tail: self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if not self.head: return "error"
        val = self.head.data
        self.head = self.head.next
        if self.head: self.head.prev = None
        else: self.tail = None
        self._size -= 1
        return val

    def pop_back(self):
        if not self.tail: return "error"
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail: self.tail.next = None
        else: self.head = None
        self._size -= 1
        return val

    def front(self):
        return self.head.data if self.head else "error"

    def back(self):
        return self.tail.data if self.tail else "error"

    def size(self): return self._size

    def clear(self):
        self.head = self.tail = None
        self._size = 0
        return "ok"

def main():
    dq = Deque()
    for line in sys.stdin:
        p = line.split()
        if not p: continue
        c = p[0]
        if c == "push_front": print(dq.push_front(p[1]))
        elif c == "push_back": print(dq.push_back(p[1]))
        elif c == "pop_front": print(dq.pop_front())
        elif c == "pop_back": print(dq.pop_back())
        elif c == "front": print(dq.front())
        elif c == "back": print(dq.back())
        elif c == "size": print(dq.size())
        elif c == "clear": print(dq.clear())
        elif c == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()