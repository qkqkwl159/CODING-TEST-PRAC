def solve(temperatures):
    temList = []
    answer= [0] * len(temperatures)

    for curDay , curTem in enumerate(temperatures):
        while temList and temList[-1][1] < curTem:
            preDay , _ = temList.pop()
            answer[preDay] = curDay - preDay
        temList.append((curDay, curTem))
    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(solve(temperatures))
