from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for x in range(n):
    graph.append(list(map(int, input().split())))

select = []
virus = []

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 바이러스와 벽이 아닌 곳 구분
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            select.append((y, x))
        elif graph[y][x] == 2:
            virus.append((y, x))

# 현재 최소 안전 영역의 크기
maxvalue = 0

# 경우의 수 선택(조합)
select = list(combinations(select, 3))

def bfs(g, start):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for move in range(4):

            tempy = v[0] + dy[move]
            tempx = v[1] + dx[move]

            if tempy < 0 or tempy >= n or tempx < 0 or tempx >= m:
                continue

            if g[tempy][tempx] == 0:
                queue.append((tempy, tempx))
                g[tempy][tempx] = 2


for tup in select:
    tempgraph = copy.deepcopy(graph)

    for i in range(3):
        y, x = tup[i][0], tup[i][1]
        tempgraph[y][x] = 1

    for k in virus:
        bfs(tempgraph, k)

    # 안전 영역 측정
    size = 0

    for y in range(n):
        for x in range(m):
            if tempgraph[y][x] == 0:
                size += 1

    maxvalue = max(maxvalue, size)

print(maxvalue)