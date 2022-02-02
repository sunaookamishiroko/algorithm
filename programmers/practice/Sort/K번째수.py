def solution(array, commands):
    answer = []

    for com in commands:
        newlist = array[com[0] - 1 : com[1]]
        newlist.sort()
        answer.append(newlist[com[2] - 1])

    return answer
