#가장 긴 정렬되어있징낳은 문제

# nums = [100, 4, 200 ,1 ,3 ,2]
nums = map(int, input().split())

longest = 0
numdic = {}

for i in nums:
    numdic[i] = 1


for num in numdic:
    prevNum = num - 1
    nextNum = num + 1
    if prevNum not in numdic:
        count=1
        while nextNum in numdic:
            count+=1
            nextNum+=1
        #연속된 수가 여러개 일때 저장되어있는 값과 방금 구한 연속된 수의 값을 비교하여 
        # 큰값을 반환 값에 저장
        longest = max(longest , count)

print(longest)
