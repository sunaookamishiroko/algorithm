from itertools import combinations

def solution(relation):
    answer = []
    sample = [x for x in range(len(relation[0]))]

    for i in range(1, len(relation[0]) + 1):
        temp = list(combinations(sample, i))

        for pick in temp:
            check = []
            for element in relation:
                temp2 = []
                for idx in pick:
                    temp2.append(element[idx])
                check.append(tuple(temp2))

            if len(check) == len(set(check)):
                signal = False
                for k in range(1, len(pick) + 1):
                    temp3 = list(combinations(pick, k))
                    for element in temp3:
                        if element in answer:
                            signal = True
                            break
                    if signal:
                        break
                if not signal:
                    answer.append(pick)

    return len(answer)