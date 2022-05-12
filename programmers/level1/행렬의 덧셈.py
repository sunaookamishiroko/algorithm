def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        answer.append([])
        for y in range(len(arr1[x])):
            answer[x].append(arr1[x][y] + arr2[x][y])


    return answer