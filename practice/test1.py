import numpy as np
import cv2
from matplotlib import pyplot as plt
# from matplotlib import pyplot as plt

imgPath = "./Screenshot 2023-12-23 at 12.31.10 AM.png"
# print(cv2.__vsersion__)

img = cv2.imread( imgPath)

plt.subplot(111)
plt.title("TEST")
plt.imshow(img)
plt.show()


arr1 = [1,2,3,4]

print(np.sum(arr1))

