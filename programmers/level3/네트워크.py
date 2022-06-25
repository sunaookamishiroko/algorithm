from collections import deque

def bfs(computers, start, visited):
    n = 0
    queue = deque([start])
    visited[start] = True
    n += 1

    while queue:
        v = queue.popleft()

        for x in range(len(computers[v])):
            if x == v:
                continue

            if computers[v][x] == 1 and not visited[x]:
                visited[v] = True
                n += 1
                queue.append(x)
    return n



def solution(n, computers):
    answer = set()

    for x in range(n):
        visited = [False] * n
        answer.add(bfs(computers, x, visited))

    return len(answer)

print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))