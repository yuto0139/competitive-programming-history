N = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
c = b[::2]
d = b[1::2]

print(sum(c) - sum(d))
