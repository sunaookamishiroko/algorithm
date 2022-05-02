def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    count = [0, 0, 0]

    for i in range(len(answers)):
        if first[i % len(first)] == answers[i]:
            count[0] += 1
        if second[i % len(second)] == answers[i]:
            count[1] += 1
        if third[i % len(third)] == answers[i]:
            count[2] += 1

    answer = []
    big = max(count)
    for k in range(3):
        if big == count[k]:
            answer.append(k + 1)

    return answer