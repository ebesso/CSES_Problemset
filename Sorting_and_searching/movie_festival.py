n = int(input())

movies = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    movies.append((a, b))

movies.sort(key=lambda a: a[1], reverse=True)

current_time = 0
count = 0

for i in range(n):
    a, b = movies.pop()
    if a >= current_time:
        current_time = b
        count += 1

print(count)
    


