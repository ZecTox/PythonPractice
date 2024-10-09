x = int(input())
ans = 0

for i in range(x):
    p, v, t = map(int, input().split())
    if p+v+t >=2:
        ans += 1
    
print(ans)