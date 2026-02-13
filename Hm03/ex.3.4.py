n = int(input())

s = bin(n)[2:]
length = len(s)

max_m = n

for i in range(1, length):
    s = s[1:] + s[0]
    current_m = int(s, 2)
    if current_m > max_m:
        max_m = current_m

print(max_m)