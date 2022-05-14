def solution(board, moves):
    answer = 0
    stack = []

    for x in moves:
        for y in range(len(board)):
            if board[y][x - 1] != 0:
                stack.append(board[y][x - 1])
                board[y][x - 1] = 0
                break

        if len(stack) >= 2 and stack[len(stack) - 1] == stack[len(stack) - 2]:
            answer += 2
            stack.pop()
            stack.pop()


    return answer