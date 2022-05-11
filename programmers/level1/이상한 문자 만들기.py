def solution(s):
    answer = ''

    li = s.split(" ")
    count = 0

    for sentense in li:
        for x in range(len(sentense)):
            if x % 2 == 0:
                answer += sentense[x].upper()
            else:
                answer += sentense[x].lower()

        count += 1
        if count != len(li):
            answer += ' '


    return answer