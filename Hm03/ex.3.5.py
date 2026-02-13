import sys
import array

def solve():
    def get_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = get_tokens()

    while True:
        try:
            line = next(tokens)
            n = int(line)

            heights = array.array('H')
            for _ in range(n):
                heights.append(int(next(tokens)))

            a = int(next(tokens))
            b = int(next(tokens))

            count = 0
            for h in heights:
                if a <= h <= b:
                    count += 1

            sys.stdout.write(str(count) + '\n')

        except StopIteration:
            break

if __name__ == "__main__":
    solve()