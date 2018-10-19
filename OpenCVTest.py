#'''
#Python2 (works with python3)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('building.jpg',0)
for xGradient in range(50,300,10):
    for yGradient in range(50,300,10):
        edges = cv2.Canny(img,xGradient,yGradient)

        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()
#'''


#shows edges
'''
#Python2 (works with python3)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('building.jpg',0)
edges = cv2.Canny(img,156,156)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
#'''


#Python3
#show grey and regualar
'''
import cv2

image = cv2.imread("building.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray_image)
cv2.imshow("Real", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
