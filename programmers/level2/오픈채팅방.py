def solution(record):
    answer = []
    uid = {}

    for rec in record:
        li = rec.split()

        if len(li) > 2:
            uid[li[1]] = li[2]

    for rec in record:
        li = rec.split()

        com = li[0]
        usrid = li[1]

        if com == "Enter":
            answer.append(uid[usrid] + "님이 들어왔습니다.")
        elif com == "Leave":
            answer.append(uid[usrid] + "님이 나갔습니다.")

    return answer