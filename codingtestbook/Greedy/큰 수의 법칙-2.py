def solution(N, M, K, array):

    array.sort()

    maxnum1 = array[N - 1]
    maxnum2 = array[N - 2]

    answer = (maxnum1 * K + maxnum2) * (M // (K + 1)) + ((M % (K + 1)) * maxnum1)

    return answer

print(solution(5, 8, 3, [2, 4, 5, 4, 6]))