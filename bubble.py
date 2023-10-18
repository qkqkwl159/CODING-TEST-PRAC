import random

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y

def bubbleSort(inputlist,elementalLength):
    for st in range(elementalLength):
        for idx in range(len(inputlist)):
            if idx == len(inputlist)-1:
                print(f'{st+1}st : {inputlist}')
                continue
            if inputlist[idx] > inputlist[idx+1]:
                inputlist[idx], inputlist[idx+1] = swap(inputlist[idx], inputlist[idx+1])
    return inputlist

def makeRandlist(elementalLength):
    randList = []
    while len(randList) != elementalLength:
        elm = random.randint(1,10)
        if elm in randList :
            continue
        randList.append(elm)
    return randList

def quickSortDevide(inputlist):
    pivot = 0
    low = 1
    high = len(inputlist)-1
    print(low,high)
    while low < high:
        while inputlist[low] < inputlist[pivot]:
            low+=1
        while inputlist[high] > inputlist[pivot]:
            high-=1
        print(low,high)
        if low > high:
            continue
        inputlist[low] , inputlist[high] = swap(inputlist[low], inputlist[high])
        print("INNER",inputlist)
    inputlist[high] , inputlist[pivot] = swap(inputlist[high], inputlist[pivot])
    returnpivot = inputlist.index(inputlist[high])

    return inputlist , returnpivot



elmLen = 10
#randList = makeRandlist(elmLen)
randList = [8 ,7 ,6, 2 ,5 ,3, 9 , 10, 1 ,4]

print(f'original : {randList}\n\n')

#print(bubbleSort(randList,elmLen))

perList , reIdx = quickSortDevide(randList)
print(perList)
perList, reIdx = quickSortDevide(perList[:reIdx])
print(perList)


