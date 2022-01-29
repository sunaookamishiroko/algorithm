def solution(participant, completion):
    dict = {}
    sumhash = 0
    for x in participant:
        dict[hash(x)] = x
        sumhash += hash(x)

    for y in completion:
        sumhash -= hash(y)

    answer = dict[sumhash]

    return answer