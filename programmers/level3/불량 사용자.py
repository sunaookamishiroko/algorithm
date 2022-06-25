from itertools import permutations

def solution(user_id, banned_id):
    answer = set()

    orders = list(permutations(user_id, len(banned_id)))

    for order in orders:
        for i in range(len(banned_id)):
            if len(order[i]) != len(banned_id[i]):
                break

            signal = False
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*':
                    continue

                if banned_id[i][j] != order[i][j]:
                    signal = True
                    break
            if signal:
                break

            if i == (len(banned_id) - 1):
                answer.add(tuple(sorted(list(order))))

    return len(answer)