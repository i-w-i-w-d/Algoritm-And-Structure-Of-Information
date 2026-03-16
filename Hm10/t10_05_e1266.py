import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    while ptr < len(input_data):
        try:
            N = int(input_data[ptr])
            T = int(input_data[ptr + 1])
            ptr += 2

            tracks = []
            for _ in range(T):
                tracks.append(int(input_data[ptr]))
                ptr += 1
        except (IndexError, ValueError):
            break

        best_sum = 0

        def backtrack(index, current_sum):
            nonlocal best_sum

            if current_sum > best_sum:
                best_sum = current_sum

            if best_sum == N:
                return

            for i in range(index, T):
                if current_sum + tracks[i] <= N:
                    backtrack(i + 1, current_sum + tracks[i])

                    if best_sum == N:
                        return

        backtrack(0, 0)

        print(f"sum:{best_sum}")

if __name__ == "__main__":
    solve()