import itertools

def solution(expression):
    answer = -1
    num = expression.replace('+', ' + ')
    num = num.replace('-', ' - ')
    num = num.replace('*', ' * ')

    stack = num.split()

    giho = []

    for i in range(len(stack)):
        if not stack[i].isnumeric():
            if stack[i] not in giho:
                giho.append(stack[i])
        else:
            stack[i] = int(stack[i])

    giho = list(itertools.permutations(giho))

    for order in giho:
        temp = stack.copy()
        for op in order:
            templist = []
            flag = False
            isnear = False
            for idx in range(len(temp)):
                if flag:
                    flag = False
                    continue

                if temp[idx] == op:
                    rightoperand = temp[idx + 1]
                    if isnear:
                        leftoperand = templist.pop()
                    else:
                        templist.pop()
                        leftoperand = temp[idx - 1]

                    if temp[idx] == '+':
                        value = leftoperand + rightoperand
                    elif temp[idx] == '-':
                        value = leftoperand - rightoperand
                    else:
                        value = leftoperand * rightoperand
                    templist.append(value)
                    flag = True
                    isnear = True
                else:
                    isnear = False
                    templist.append(temp[idx])

            temp = templist.copy()
        answer = max(answer, abs(temp[0]))

    return answer