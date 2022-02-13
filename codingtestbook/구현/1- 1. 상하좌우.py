n = int(input())
mapList = input().split()
xpos = 1
ypos = 1

for move in mapList:
    if move == "R" and ypos != n:
        ypos += 1
    elif move == "L" and ypos != 1:
        ypos -= 1
    elif move == "U" and xpos != 1:
        xpos -= 1
    elif move == "D" and xpos != n:
        xpos += 1

print(xpos, ypos)