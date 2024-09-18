n = int(input())

tasks = []
t = 0

for _ in range(n):
    a, d = list(map(int, input().split()))
    tasks.append([a, d])

tasks.sort(key=lambda x: x[0])

reward = 0

for i in range(n):
    a, d = tasks[i]
    t += a
    reward += d - t

print(reward)

