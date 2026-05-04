import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class SegmentTreeGCD:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) // 2
            self._build(data, 2 * v, tl, tm)
            self._build(data, 2 * v + 1, tm + 1, tr)
            self.tree[v] = gcd(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = gcd(self.tree[2 * v], self.tree[2 * v + 1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return gcd(self.query(2 * v, tl, tm, l, min(r, tm)),
                   self.query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    n = int(input_data[0])
    arr = list(map(int, input_data[1:n + 1]))
    m = int(input_data[n + 1])

    st = SegmentTreeGCD(arr)

    idx = n + 2
    results = []
    for _ in range(m):
        type_q = int(input_data[idx])
        l_val = int(input_data[idx + 1])
        r_val = int(input_data[idx + 2])
        idx += 3

        if type_q == 1:
            results.append(str(st.query(1, 0, n - 1, l_val - 1, r_val - 1)))
        else:
            st.update(1, 0, n - 1, l_val - 1, r_val)

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()