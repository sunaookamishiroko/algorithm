def solution(numbers, hand):
    answer = ''

    location = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    lefthand = [3, 0]
    righthand = [3, 2]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            lefthand[0], lefthand[1] = location[num][0], location[num][1]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            righthand[0], righthand[1] = location[num][0], location[num][1]
        else:
            leftlocation = abs(lefthand[0] - location[num][0]) + abs(lefthand[1] - location[num][1])
            rightlocation = abs(righthand[0] - location[num][0]) + abs(righthand[1] - location[num][1])

            signal = -1

            if leftlocation < rightlocation:
                signal = 0
            elif leftlocation > rightlocation:
                signal = 1
            else:
                if hand == "left":
                    signal = 0
                else:
                    signal = 1

            if signal == 0:
                answer += 'L'
                lefthand[0], lefthand[1] = location[num][0], location[num][1]
            else:
                answer += 'R'
                righthand[0], righthand[1] = location[num][0], location[num][1]

    return answer