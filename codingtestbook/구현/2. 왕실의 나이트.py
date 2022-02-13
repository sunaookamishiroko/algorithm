location = list(input())

xpos = ord(location[0]) - 96
ypos = int(location[1])
count = 0

moveList = [(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (-1, 2), (1, -2), (-1, -2)]

for move in moveList:
    x = xpos + move[0]
    y = ypos + move[1]

    if not (x < 1 or x > 8 or \
            y < 1 or y > 8):
        count += 1
print(count)