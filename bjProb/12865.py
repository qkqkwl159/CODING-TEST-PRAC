setDic = {}
answer = 0

inputValue= list(map(int, input().split()))

for n in range(inputValue[0]):
    setValue = list(map(int , input().split()))
    if setValue[0] not in setDic:
        setDic[setValue[0]] = setValue[1]

for r in setDic:
    if inputValue[0] >= r:
        answer += setDic[r]

print(answer)
