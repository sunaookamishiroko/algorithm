def solution(msg):
    answer = []
    dic = {}
    init = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(init)):
        dic[init[x]] = x + 1

    left = 0
    right = 0
    idx = 27

    while True:

        if msg[left:right + 1] in dic:
            if right == len(msg) - 1:
                answer.append(dic[msg[left:right + 1]])
                break
            right += 1
            continue
        else:
            answer.append(dic[msg[left:right]])
            dic[msg[left:right + 1]] = idx
            idx += 1
            left = right

    return answer