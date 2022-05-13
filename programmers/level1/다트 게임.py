def solution(dartResult):
    previous = -1
    now = -1
    answer = [-1, -1, -1]

    for x in dartResult:
        if x.isnumeric():
            if answer[now] == 1 and x == '0':
                answer[now] = 10
                continue
            if now != -1:
                previous += 1
            now += 1
            answer[now] = int(x)
        elif x.isalpha():
            if x == 'D':
                answer[now] = answer[now] ** 2
            elif x == 'T':
                answer[now] = answer[now] ** 3
        else:
            if x == '*':
                answer[now] *= 2
                if previous != -1:
                    answer[previous] *= 2
            else:
                answer[now] *= -1

    return sum(answer)