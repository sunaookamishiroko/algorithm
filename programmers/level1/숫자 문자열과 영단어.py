def solution(s):
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for x in range(len(english)):
        s = s.replace(english[x], str(x))
    return int(s)