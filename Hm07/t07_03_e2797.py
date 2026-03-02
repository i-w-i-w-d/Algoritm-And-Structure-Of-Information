import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())

    phone_numbers = []
    while len(phone_numbers) < n:
        line = sys.stdin.readline()
        if not line:
            break
        phone_numbers.extend(line.split())

    unique_contacts = set(phone_numbers[:n])
    print(len(unique_contacts))

if __name__ == '__main__':
    solve()