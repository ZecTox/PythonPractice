k, n, w = map(int, input().split())

total_cost = 0

for i in range(w):
    total_cost += k * (i + 1)

if total_cost <= n:
    print(0)
else:
    final_ans = total_cost - n 
    print(final_ans)
