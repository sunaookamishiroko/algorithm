from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for count in range(m):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])

# visited -> distance로 대체
queue = deque([x])
distance = [-1] * (n + 1)
distance[x] = 0

count = 1

while queue:
    v = queue.popleft()

    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = count
            queue.append(i)
    count += 1

check = False

for index in range(1, len(distance)):
    if distance[index] == k:
        print(index)
        check = True

if check == False:
    print(-1)