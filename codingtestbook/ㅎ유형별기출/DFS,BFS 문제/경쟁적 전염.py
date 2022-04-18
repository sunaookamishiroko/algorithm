from collections import deque

n, k = map(int, input().split())

arr = []
info = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    # 바이러스 정보를 저장
    for j in range(n):
        if arr[i][j] != 0:
            # 바이러스 숫자, 초, y, x
            info.append((arr[i][j], 0, i, j))

s, x, y = map(int, input().split())

# 바이러스 숫자 기준으로 정렬
info.sort()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque(info)

while queue:
    t_value, t_s, t_y, t_x = queue.popleft()

    if t_s == s:
        break

    for index in range(4):
        newy = t_y + dy[index]
        newx = t_x + dx[index]
        if newy <= -1 or newy >= n or newx <= -1 or newx >= n:
            continue

        if arr[newy][newx] == 0:
            arr[newy][newx] = t_value
            queue.append((arr[newy][newx], t_s + 1, newy, newx))

print(arr[x - 1][y - 1])