bookDic = {}
repeatNum = int(input())
for _ in range(repeatNum):
    bookName = input()
    if bookName in bookDic:
        bookDic[bookName] += 1
    else:
        bookDic[bookName] = 1


maxv = 0
bestSeller = dict( sorted(bookDic.items()) )
for b in bestSeller:
    if (bestSeller[b]) > maxv:
        maxv = bestSeller[b]
        maxvi = b
print(maxvi)
