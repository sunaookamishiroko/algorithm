import bisect, itertools, collections

def solution(info, query):
    dic = collections.defaultdict(list)
    binary = list(itertools.product((True, False), repeat=4))

    for i in info:
        i = i.split()
        for sig in binary:
            key = ''
            for k in range(4):
                if sig[k]:
                    key += i[k]
                else:
                    key += '-'
            dic[key].append(int(i[4]))

    for k in dic.keys():
        dic[k].sort()

    answer = []
    for q in query:
        a, _, b, _, c, _, d, e = q.split()
        key = a + b + c + d

        i = bisect.bisect_left(dic[key], int(e))
        answer.append(len(dic[key]) - i)


    return answer