def solution(progresses, speeds):
    persent = list(progresses)
    order = 0
    answer = []

    while order < len(progresses):
        num = 0
        for x in range(len(persent)):
            if not persent[x] >= 100:
                persent[x] = persent[x] + speeds[x]
        for y in range(len(persent)):
            if persent[y] >= 100 and y == order:
                num += 1
                order += 1
        if num != 0:
            answer.append(num)
    return answer