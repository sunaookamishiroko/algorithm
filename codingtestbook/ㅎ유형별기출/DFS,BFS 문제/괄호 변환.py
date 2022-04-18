def solution(p):
    # 1. 빈 문자열 반환
    if p == '':
        return p

    # 2. 문자열 w를 균형잡힌 문자열 u, v로 분리
    count = 0
    idx = -1
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            idx = i
            break
    u = p[:idx+1]
    v = p[idx+1:]

    # u가 올바른 괄호 문자열인지 판단
    stack = []
    signal = False

    for ele in u:
        if ele == '(':
            stack.append(ele)
        else:
            if len(stack) == 0:
                signal = True
                break
            stack.pop()

    if len(stack) != 0:
        signal = True

    # 4. 문자열 u가 올바른 괄호 문자열이 아닌 경우
    if signal:
        empty = '(' + solution(v) + ')'

        # 첫 번째와 마지막 문자를 제거
        u = list(u[1:-1])

        # 괄호 뒤집기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        return empty + ''.join(u)
    # 3. 문자열 u가 올바른 괄호 문자열인 경우
    else:
        return u + solution(v)