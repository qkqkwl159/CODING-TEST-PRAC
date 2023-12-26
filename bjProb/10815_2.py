haveCardNum = int(input())
haveCard = list(map(int, input().split()))

# haveCard = list( haveCard )

setCardNum = int(input())
setCard = list(map(int, input().split()))


haveCardDic = {}

for c in  haveCard:
    if c not in haveCardDic:
        haveCardDic[c] = 0

print(haveCardDic)

for  c in setCard:
    if c in haveCardDic:
        haveCardDic[c] = 1
    else:
        haveCardDic[c] = 0

print(haveCardDic)
for r in haveCardDic:
    print(haveCardDic[r] , end=' ')

