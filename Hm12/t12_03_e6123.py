import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        print("ok")

    def pop(self):
        if not self.items:
            print("error")
        else:
            print(self.items.pop())

    def back(self):
        if not self.items:
            print("error")
        else:
            print(self.items[-1])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print("ok")

def solve():
    stack = Stack()
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        command = parts[0]

        if command == "push":
            stack.push(int(parts[1]))
        elif command == "pop":
            stack.pop()
        elif command == "back":
            stack.back()
        elif command == "size":
            stack.size()
        elif command == "clear":
            stack.clear()
        elif command == "exit":
            print("bye")
            break

if __name__ == "__main__":
    solve()