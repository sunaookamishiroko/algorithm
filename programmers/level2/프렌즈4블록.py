def solution(m, n, board):
    dx = [1, -1, 1, -1]
    dy = [1, 1, -1, -1]

    answer = 0
    temp = []

    for y in range(m):
        temp.append(list(board[y]))

    board = temp

    while True:
        temp = []

        for y in range(m):
            for x in range(n):
                for idx in range(4):

                    if x + dx[idx] > n - 1 or x + dx[idx] < 0:
                        continue
                    if y + dy[idx] > m - 1 or y + dy[idx] < 0:
                        continue
                    if board[y][x] is None:
                        continue

                    if board[y][x] == board[y][x + dx[idx]] \
                            and board[y][x] == board[y + dy[idx]][x] \
                            and board[y][x] == board[y + dy[idx]][x + dx[idx]]:

                        temp.append((y, x + dx[idx]))
                        temp.append((y + dy[idx], x))
                        temp.append((y + dy[idx], x + dx[idx]))

        answer += len(set(temp))

        if len(temp) == 0:
            return answer

        for y, x in set(temp):
            board[y][x] = None

        for x in range(n):
            stack = []
            startindex = -1
            for y in range(m - 1, -1, -1):
                if board[y][x] is None:
                    if startindex == -1:
                        startindex = y
                else:
                    if startindex != -1:
                        stack.append((y, x))

            if len(stack) > 0:
                for y in range(startindex, -1, -1):
                    tempy, tempx = stack.pop(0)
                    board[y][x] = board[tempy][tempx]
                    board[tempy][tempx] = None
                    if len(stack) == 0:
                        break

