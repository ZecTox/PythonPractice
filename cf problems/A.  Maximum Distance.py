N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_distance = 0

for i in range(N):
    for j in range(i+1, N):
        coordinate_max_distance = (x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2
        max_distance = max(max_distance, coordinate_max_distance)

print(max_distance)