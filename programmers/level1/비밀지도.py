def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        map1 = bin(arr1[i])
        map2 = bin(arr2[i])

        if len(map1) != n + 2:
            map1 = '0' * ((n + 2) - len(map1)) + map1[2:]
        else:
            map1 = map1[2:]

        if len(map2) != n + 2:
            map2 = '0' * ((n + 2) - len(map2)) + map2[2:]
        else:
            map2 = map2[2:]

        temp = ''
        for j in range(n):
            if map1[j] == '1' or map2[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer