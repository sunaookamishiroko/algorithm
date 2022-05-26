import collections

def solution(s):
    answer = []
    s = s.replace("{", "")
    s = s.replace("}", "")

    count = collections.Counter(s.split(",")).most_common()

    for x in count:
        answer.append(int(x[0]))

    return answer