def solution(n, t, m, timetable):
    arrive = [60 * 9]
    dic = {}
    dic[60 * 9] = []

    for x in range(n - 1):
        arrive.append(arrive[x] + t)
        dic[arrive[x] + t] = []

    for time in sorted(timetable):
        time = int(time[:2]) * 60 + int(time[3:])

        if time > arrive[-1]:
            continue

        for x in range(len(arrive)):
            if arrive[x] >= time and len(dic[arrive[x]]) < m:
                dic[arrive[x]].append(time)
                dic[arrive[x]].sort()
                break

    if len(dic[arrive[-1]]) != m:
        t = arrive[-1]
    else:
        t = dic[arrive[-1]][-1] - 1

    return '%02d:%02d' % (t // 60, t % 60)