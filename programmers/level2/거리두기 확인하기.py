def solution(places):
    answer = []
    dy = [-1, 1, 0, 0, 2, -2, 0, 0, -1, 1, 1, -1]
    dx = [0, 0, -1, 1, 0, 0, 2, -2, 1, 1, -1, -1]

    for place in places:
        temp = []
        for ele in place:
            temp.append(list(ele))

            flag = False
        for i in range(5):
            for j in range(5):
                if temp[i][j] == 'P':
                    for k in range(12):
                        tempy = i + dy[k]
                        tempx = j + dx[k]

                        if tempy < 0 or tempy > 4 or tempx < 0 or tempx > 4:
                            continue

                        if temp[tempy][tempx] == 'P':
                            if 0 <= k <= 3:
                                flag = True
                                break
                            elif 4 <= k <= 5:
                                if dy[k] > 0:
                                    value = -1
                                else:
                                    value = 1

                                if temp[tempy + value][tempx] != 'X':
                                    flag = True
                                    break
                            elif 6 <= k <= 7:
                                if dx[k] > 0:
                                    value = -1
                                else:
                                    value = 1

                                if temp[tempy][tempx + value] != 'X':
                                    flag = True
                                    break
                            elif 8 <= k <= 11:
                                check = (i - tempy, j - tempx)

                                if temp[tempy + check[0]][tempx] != 'X' or temp[tempy][tempx + check[1]] != 'X':
                                    flag = True
                                    break


                if flag:
                    break
            if flag:
                break

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer