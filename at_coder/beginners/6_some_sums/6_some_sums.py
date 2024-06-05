n, a, b = map(int, input().split())
s = 0

for i in range(1, n + 1):
    ans = sum(map(int, str(i)))
    if a <= ans <= b:
        s += i

print(s)
