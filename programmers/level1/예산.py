def solution(d, budget):
    d.sort()
    answer = 0
    temp = 0

    for price in d:
        if temp + price <= budget:
            temp += price
            answer += 1
        else:
            break
    return answer