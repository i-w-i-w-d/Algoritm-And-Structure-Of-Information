import sys

sys.setrecursionlimit(200000)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class SegmentTreeWin:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def combine(self, left, right):
        g = gcd(left[0], right[0])
        is_same = left[1] and right[1] and left[0] == right[0]
        return (g, is_same)

    def _build(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = (data[tl], True)
        else:
            tm = (tl + tr) // 2
            self._build(data, 2 * v, tl, tm)
            self._build(data, 2 * v + 1, tm + 1, tr)
            self.tree[v] = self.combine(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = (new_val, True)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = self.combine(self.tree[2 * v], self.tree[2 * v + 1])

    def query(self, v, tl, tr, l, r):
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        if r <= tm:
            return self.query(2 * v, tl, tm, l, r)
        elif l > tm:
            return self.query(2 * v + 1, tm + 1, tr, l, r)
        else:
            left_res = self.query(2 * v, tl, tm, l, tm)
            right_res = self.query(2 * v + 1, tm + 1, tr, tm + 1, r)
            return self.combine(left_res, right_res)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    n = int(input_data[ptr])
    ptr += 1

    arr = list(map(int, input_data[ptr: ptr + n]))
    ptr += n

    m = int(input_data[ptr])
    ptr += 1

    st = SegmentTreeWin(arr)
    results = []

    for _ in range(m):
        q = int(input_data[ptr])
        l_idx = int(input_data[ptr + 1])
        r_idx = int(input_data[ptr + 2])
        ptr += 3

        if q == 1:
            res_gcd, is_draw = st.query(1, 0, n - 1, l_idx - 1, r_idx - 1)
            results.append("draw" if is_draw else "wins")
        else:
            st.update(1, 0, n - 1, l_idx - 1, r_idx)

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()