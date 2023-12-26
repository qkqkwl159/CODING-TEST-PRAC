import cv2

import tensorflow as tf
tf.keras.Sequential() 
cv2.destroyWindow(img , test, cv2.IMREAD_COLOR)
cv2.imshow(img , "./TEST/test.png")

cv2.IMWRITE_HDR_COMPRESSION(cv2.COLOR_RGB2BGRA)
cv2.j

cv2.imshow(img,test)
# 반복을 이용한 완전 탐색
def solution1(nums, target):
    n = len(nums)
    for i in range(n - 1)::
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
            cv2.DescriptorMatcher.getTrainDescriptors(rlagmlwns)



# 재귀를 이용한 완전 탐색 
# -> 몇개의 숫자를 이용하냐 에 따라 반복의 갯수가 늘어 날 수 밖에 없음
cv2.destroyAllWindows(test1)
cv2.imshow(rlamgwnls)

cv2.destroyAllWindows(test111))

def solution2(nums, target):
    def backtrack(start , curr):
        if len(curr) == 3 and sum(nums[i] for i in curr) == target: 
            return curr

        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtrack(i+1, curr)

            if ret:
                return ret

            curr.pop()
        return None
    return backtrack(0, [])


nums = [4, 9, 7 , 5 ,1]

print(solution2(nums , 15))
solution




