def solution(fees, records):
    answer = []

    time = {}
    cost = {}

    for record in records:
        record = record.split()

        if record[2] == "IN":
            if record[1] not in time:
                cost[record[1]] = 0

            time[record[1]] = ["IN", record[0]]
        else:
            start = time[record[1]][1]
            end = record[0]

            cost[record[1]] += ((int(end[:2]) - int(start[:2])) * 60) + (int(end[3:]) - int(start[3:]))
            time[record[1]][0] = "OUT"

    for key in sorted(time.keys()):

        if time[key][0] == "IN":
            start = time[key][1]
            alltime = (23 - int(start[:2])) * 60 + (59 - int(start[3:])) + cost[key]
        else:
            alltime = cost[key]

        alltime -= fees[0]

        if alltime <= 0:
            answer.append(fees[1])
            continue
        else:
            if alltime % fees[2] != 0:
                temp = int(fees[1] + (alltime // fees[2] + 1) * fees[3])
            else:
                temp = int(fees[1] + (alltime / fees[2]) * fees[3])
            answer.append(temp)

    return answer