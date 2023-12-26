def twoSum(nums , target):
    memo = {}
    for v in nums:
        memo[v] = 1

    for v in nums:
        needNumber = target -v 
        if needNumber in memo:
            return True
    return False


nums = [4, 1, 9 ,7 ,5, 3, 16]
print(twoSum(nums, 14))
