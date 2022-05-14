def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    replc = []
    for x in range(len(new_id)):
        if not new_id[x].isalnum() and new_id[x] != '-' and new_id[x] != '_' and new_id[x] != '.':
            replc.append(new_id[x])

    for x in set(replc):
        new_id = new_id.replace(x, '')
    # 3
    machim = []
    now = ''
    for x in new_id:
        if x == '.':
            now += '.'
        else:
            if len(now) > 1:
                machim.append(now)
            now = ''
    if len(now) > 1:
        machim.append(now)

    machim.sort(reverse=True)

    for x in machim:
        new_id = new_id.replace(x, '.')
    # 4
    if len(new_id) >= 2:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif len(new_id) == 1:
        if new_id[0] == '.':
            new_id = ''
    # 5
    if new_id == '':
        new_id += 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7
    if len(new_id) <= 2:
        letter = new_id[-1]
        while True:
            new_id += letter
            if len(new_id) == 3:
                break

    return new_id