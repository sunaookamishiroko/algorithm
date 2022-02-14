n, m = map(int, input().split())
xpos, ypos, direction = (map(int, input().split()))
mapList = []

isVisit = [(xpos, ypos)]
answer = 1
moveCount = 0

for i in range(n):
    temp = list(map(int, input().split()))
    mapList.append(temp)

while True:
    if direction == 0:
        direction = 3
    else:
        direction -= 1

    if direction == 0:
        if moveCount == 4:
            if mapList[ypos + 1][xpos] != 1:
                ypos += 1
                continue
            else:
                break

        if ypos - 1 >= 0 and mapList[ypos - 1][xpos] != 1 and (xpos, ypos - 1) not in isVisit:
            ypos -= 1
            answer += 1
            moveCount = 0
            isVisit.append((xpos, ypos))
        else:
            moveCount += 1

    elif direction == 1:
        if moveCount == 4:
            if mapList[ypos][xpos - 1] != 1:
                xpos -= 1
                continue
            else:
                break

        if xpos + 1 <= m and mapList[ypos][xpos + 1] != 1 and (xpos + 1, ypos) not in isVisit:
            xpos += 1
            answer += 1
            moveCount = 0
            isVisit.append((xpos, ypos))
        else:
            moveCount += 1
    elif direction == 2:
        if moveCount == 4:
            if mapList[ypos - 1][xpos] != 1:
                ypos -= 1
                continue
            else:
                break

        if ypos + 1 <= n and mapList[ypos + 1][xpos] != 1 and (xpos, ypos + 1) not in isVisit:
            ypos += 1
            answer += 1
            moveCount = 0
            isVisit.append((xpos, ypos))
        else:
            moveCount += 1
    elif direction == 3:
        if moveCount == 4:
            if mapList[ypos][xpos + 1] != 1:
                xpos += 1
                continue
            else:
                break
        if xpos - 1 >= 0 and mapList[ypos][xpos - 1] != 1 and (xpos - 1, ypos) not in isVisit:
            xpos -= 1
            answer += 1
            moveCount = 0
            isVisit.append((xpos, ypos))
        else:
            moveCount += 1

print(answer)