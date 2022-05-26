import collections

def solution(cacheSize, cities):
    answer = 0
    q = collections.deque([])

    for city in cities:
        city = city.lower()

        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            if cacheSize != 0:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(city)
            answer += 5

    return answer