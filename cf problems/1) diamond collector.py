n, k = map(int, input().split())
arr = []
max_diamonds = 0

for _ in range(n):
    arr.append(int(input()))

for i in arr:
    count = 0
    for j in arr:
        if i <= j <= i + k:
            count += 1
    max_diamonds = max(max_diamonds, count)

print(max_diamonds)