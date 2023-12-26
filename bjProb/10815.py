haveCardNum = int(input())
haveCard = list(map(int, input().split()))

# haveCard = list( haveCard )

setCardNum = int(input())
setCard = list(map(int, input().split()))

answer = [0] * len(setCard)

haveCardDic = {}
for c in  haveCard:
    if c not in haveCardDic:
        haveCardDic[c] = 1



for cindex , c in enumerate(setCard):
    if c in haveCardDic:
        answer[cindex] = 1

for r in answer:
    print(r , end=' ')

