def solution(s):
    length = len(s) // 2
    result = len(s)

    for step in range(1, length + 1):

        temp = s[0:step]
        sentence = ""
        count = 1

        for j in range(step, len(s), step):
            # 지금 갖고있는 문자열이 다음 문자열과 같으면 count++
            if temp == s[j:j+step]:
                count += 1
            # 같지 않으면 문자열 만들기
            # 그리고 temp는 이제 바로 그 같지 않은 문자열이 되어서 그 문자열로 같은지 체크하기 시작
            else:
                if count != 1:
                    sentence += (str(count) + temp)
                else:
                    sentence += temp
                temp = s[j:j+step]
                count = 1

        # 남아 있는 문자열 처리
        if count != 1:
            sentence += (str(count) + temp)
        else:
            sentence += temp

        result = min(result, len(sentence))

    return result