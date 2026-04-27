import sys

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.pos = {}

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i][0]] = i
        self.pos[self.heap[j][0]] = j

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] > self.heap[parent][1]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            if right < n and self.heap[right][1] > self.heap[largest][1]:
                largest = right

            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break

    def add(self, id_, priority):
        self.heap.append([id_, priority])
        idx = len(self.heap) - 1
        self.pos[id_] = idx
        self.sift_up(idx)

    def pop(self):
        if not self.heap:
            return None
        max_elem = self.heap[0]
        id_ = max_elem[0]
        del self.pos[id_]

        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.pos[last[0]] = 0
            self.sift_down(0)

        return max_elem

    def change(self, id_, new_priority):
        idx = self.pos[id_]
        old_priority = self.heap[idx][1]
        self.heap[idx][1] = new_priority
        if new_priority > old_priority:
            self.sift_up(idx)
        elif new_priority < old_priority:
            self.sift_down(idx)

def main():
    lines = sys.stdin.read().splitlines()
    pq = PriorityQueue()

    for line in lines:
        if not line.strip():
            continue
        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD":
            pq.add(parts[1], int(parts[2]))
        elif cmd == "POP":
            elem = pq.pop()
            if elem:
                print(f"{elem[0]} {elem[1]}")
        elif cmd == "CHANGE":
            pq.change(parts[1], int(parts[2]))

if __name__ == '__main__':
    main()