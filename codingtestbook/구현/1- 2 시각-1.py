n = int(input())
hour = 0
minute = 0
sec = 0
count = 0
checkList = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

while hour <= n:
    for x in checkList:
        if hour == x or minute == x or sec == x:
            count += 1
            break
    sec += 1
    if sec == 60:
        sec = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1

print(count)