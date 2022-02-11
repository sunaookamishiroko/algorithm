def solution(N, M, K, array):
    answer = 0
    count = 0

    array.sort()

    maxnum1 = array[N - 1]
    maxnum2 = array[N - 2]

    for x in range(M):
        count += 1
        if count > K:
            answer += maxnum2
            count = 0
        else:
            answer += maxnum1
    return answer

print(solution(5, 8, 3, [2, 4, 5, 4, 6]))