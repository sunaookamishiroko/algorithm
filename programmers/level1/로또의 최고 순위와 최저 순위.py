def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    top = 0
    bottom = 0

    for i in lottos:
        if i == 0:
            top += 1
            continue
        for j in win_nums:
            if i == j:
                top += 1
                bottom += 1

    return [rank[top], rank[bottom]]