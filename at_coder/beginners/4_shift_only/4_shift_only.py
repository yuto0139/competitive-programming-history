input()
L = list(map(int, input().split()))
cnt = 0

while all(e % 2 == 0 for e in L):
    L = [e // 2 for e in L]
    cnt += 1

print(cnt)
