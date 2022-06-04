def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1set = []
    str2set = []

    for i in range(len(str1) - 1):
        temp = str1[i:i + 2]
        if temp.isalpha():
            str1set.append(temp)

    for i in range(len(str2) - 1):
        temp = str2[i:i + 2]
        if temp.isalpha():
            str2set.append(temp)

    hap = 0
    gyo = 0

    for string in set(str1set + str2set):
        hap += max(str1set.count(string), str2set.count(string))
        gyo += min(str1set.count(string), str2set.count(string))

    if gyo == 0 and hap == 0:
        answer = 1
    else:
        answer = gyo / hap

    return int(answer * 65536)