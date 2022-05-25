import collections, itertools

def solution(orders, course):
    answer = []
    for i in course:
        big = 0
        dic = collections.defaultdict(int)
        for order in orders:

            select = itertools.combinations(sorted(list(order)), i)
            for li in select:
                key = ''
                for alpha in li:
                    key += alpha
                dic[key] += 1
                big = max(big, dic[key])
        if big < 2:
            continue
        for key, value in dic.items():
            if value == big:
                answer.append(key)
    answer.sort()
    return answer