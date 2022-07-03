def solution(files):
    answer = []
    temp = []
    for file in files:
        signal = False
        startidx = -1
        endidx = len(file)
        for i in range(len(file)):
            if file[i].isdigit():
                if not signal:
                    startidx = i
                    signal = True
            else:
                if signal:
                    endidx = i
                    break
        temp.append((file[:startidx].lower(), int(file[startidx:endidx]), file))

    temp.sort(key = lambda x: (x[0], x[1]))

    for ele in temp:
        answer.append(ele[2])

    return answer