def convert(string):
    string = list(string)
    temp = []

    for x in range(len(string)):
        if string[x] == '#':
            temp[len(temp) - 1] = temp[len(temp) - 1].lower()
        else:
            temp.append(string[x])

    return ''.join(temp)

def solution(m, musicinfos):
    answer = "(None)"
    playtime = -1

    m = convert(m)

    for info in musicinfos:
        info = info.split(",")
        start, end, songname, songcode = info
        time = (int(end[3:]) - int(start[3:])) + 60 * (int(end[:2]) - int(start[:2]))

        songcode = convert(songcode)
        songcode = songcode * (time // len(songcode)) + songcode[:time % len(songcode)]

        startindex = songcode.find(m)
        if startindex != -1 and time > playtime:
            answer = songname
            playtime = time

    return answer