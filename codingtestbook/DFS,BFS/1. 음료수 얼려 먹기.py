n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

icecream = 0


def dfs(graph, y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1

        dfs(graph, y + 1, x)
        dfs(graph, y - 1, x)
        dfs(graph, y, x + 1)
        dfs(graph, y, x - 1)
        return True
    else:
        return False


for y in range(n):
    for x in range(m):
        if graph[y][x] != 1:
            if dfs(graph, y, x):
                icecream += 1

print(icecream)