import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    pointer = 0
    while pointer < len(input_data):
        v_max = int(input_data[pointer])
        d = int(input_data[pointer + 1])
        n = int(input_data[pointer + 2])
        pointer += 3

        if n == 0:
            print("00:00")
            continue

        X = []
        T = []
        for _ in range(n):
            X.append(int(input_data[pointer]))
            t_str = input_data[pointer + 1]
            h, m = map(int, t_str.split(':'))
            T.append((h * 60 + m) * v_max)
            pointer += 2

        d_v = d * v_max
        INF = 10 ** 18
        best_V = [INF] * (n + 1)
        last_dp = [0] * (n + 1)

        for i in range(n):
            x_i = X[i]
            t_i_v = T[i]

            for k in range(i + 1, 1, -1):
                dp_k = best_V[k - 1] + x_i
                if t_i_v > dp_k:
                    dp_k = t_i_v
                dp_k += d_v
                last_dp[k] = dp_k

                val = dp_k - x_i
                if val < best_V[k]:
                    best_V[k] = val

            dp_1 = x_i
            if t_i_v > dp_1:
                dp_1 = t_i_v
            dp_1 += d_v
            last_dp[1] = dp_1

            val = dp_1 - x_i
            if val < best_V[1]:
                best_V[1] = val

        ans_scaled = INF
        last_X = X[-1]
        for k in range(1, n + 1):
            time_scaled = last_dp[k] + (n - k) * d_v + last_X
            if time_scaled < ans_scaled:
                ans_scaled = time_scaled

        total_minutes = (ans_scaled + v_max - 1) // v_max
        hours = (total_minutes // 60) % 24
        minutes = total_minutes % 60

        print(f"{hours:02d}:{minutes:02d}")


if __name__ == "__main__":
    solve()