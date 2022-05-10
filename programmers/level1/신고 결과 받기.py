def solution(id_list, report, k):
    check = [[0] * len(id_list) for _ in range(len(id_list))]
    count = [0] * len(id_list)
    answer = [0] * len(id_list)

    for sentense in report:
        a, b = sentense.split()

        aindex = id_list.index(a)
        bindex = id_list.index(b)


        if check[aindex][bindex] == 0:
            count[bindex] += 1
            check[aindex][bindex] += 1

    for x in range(len(count)):
        if count[x] >= k:
            for y in range(len(id_list)):
                if check[y][x] == 1:
                    answer[y] += 1

    return answer