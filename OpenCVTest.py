
manyBuildingPic = 'some_houses.png'
oneBuildingPic = 'building.jpg'



import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

xGradient = 87
yGradient = xGradient

im = cv.imread(manyBuildingPic)
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
edges = cv.Canny(imgray, xGradient, yGradient)  #100,200
minLineLength = 45 # Changing this to 100 does nothing.
maxLineGap = 1
threshold = 50
minLineLengthSquared = 100

lines = cv.HoughLinesP(edges,1,np.pi/180,threshold,minLineLength,maxLineGap)
for l in lines:
    for x1,y1,x2,y2 in l:
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 > minLineLengthSquared:
            cv.line(im,(x1,y1),(x2,y2),(0,0,255), 2)
plt.imshow(im)
plt.title('xGradient {}, yGradient {}'.format(xGradient, yGradient)), plt.xticks([]), plt.yticks([])
plt.show()














#loop through a bunch of gradient levels for an image in the same local directory
'''
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
        plt.title('xGradient {}, yGradient {}'.format(xGradient, yGradient)), plt.xticks([]), plt.yticks([])

        plt.show()
#'''


'''
#Contours
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

im = cv.imread('building.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

for threshold in range(0, 200, 5):
    #for maxthresh in range(0, 2000, 100):
    maxthresh = 1000
    ret, thresh = cv.threshold(imgray, threshold, maxthresh, 0)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(im, contours, -1, (0,255,0), 3)
    plt.imshow(im)
    plt.title('threshold {}, maxthresh {}'.format(threshold, maxthresh)), plt.xticks([]), plt.yticks([])
    plt.show()



#'''


#BROKEN TODO - to similate a slider with keyboard input
#shows edges of a single image in the same local directory
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('building.jpg',0)

gradient = 150

while True:
    edges = cv2.Canny(img, gradient, gradient)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    #plt.show()
    input()


def showPlot(plt):
    plt.show()

#'''




#shows edges of a single image in the same local directory
'''
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
