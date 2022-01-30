def solution(priorities, location):
    seqlist = []
    answerlist = []

    for x in range(0, len(priorities)):
        seqlist.append(x)

    while len(priorities) != 0:

        if priorities[0] < max(priorities):
            seqlist.append(seqlist.pop(0))
            priorities.append(priorities.pop(0))
        else:
            temp = seqlist.pop(0)
            if temp == location:
                return len(answerlist) + 1
            else:
                answerlist.append(temp)
                priorities.pop(0)