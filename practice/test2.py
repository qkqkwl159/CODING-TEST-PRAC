def solve(temperatures):
    answer = [0] * len(temperatures)
    stackList = list()

    for curDay, curTem in enumerate(temperatures):
        while stackList and stackList[-1][1] < curTem:
            prevDay , _ = stackList.pop()
            answer[prevDay] = curDay  - prevDay
        stackList.append((curDay, curTem))
    return answer




temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print( solve(temperatures) )
