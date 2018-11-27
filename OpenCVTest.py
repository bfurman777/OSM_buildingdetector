
manyBuildingPic = 'some_houses.png'
oneBuildingPic = 'building.jpg'
apiKey_MapBox = 'pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNqZGFrZ2c2dzFlMWgyd2x0ZHdmMDB6NzYifQ.9Pl3XOO82ArX94fHV289Pg'



'''GETTING IMAGES # TODO (From James's ):

"""Contains functions dealing with geolocation. This is mostly used for finding
coordinates from Slippy Map tiles and vice versa.  Slippy Map tiles are used in
aerial imagery APIs.
 For more information (and for the source of some of these functions) see
https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
"""
import math
def deg2tile(lat_deg, lon_deg, zoom):
    """Converts coordinates into the nearest x,y Slippy Map tile"""
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad)))
                 / math.pi) / 2.0 * n)
    return (xtile, ytile)
def tile2deg(xtile, ytile, zoom):
    """Returns the coordinates of the northwest corner of a Slippy Map
    x,y tile"""
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)



"""Interface for downloading aerial imagery from Mapbox.
"""
import requests
from PIL import Image
from io import BytesIO
from geolocation import *
class ImageryDownloader(object):
    def __init__(self, access_token):
        """Initializes the object with a Mapbox access token"""
        self.access_token = access_token

    def download_tile(self, x, y, zoom):
        """Downloads a map tile as an image.
           Note that x and y refer to Slippy Map coordinates.
        """
        url = "https://a.tiles.mapbox.com/v4/digitalglobe.316c9a2e/" \
               "" + str(zoom) + "/" + str(x) + "/" + str(y) + "" \
               ".png?access_token=" + self.access_token
        req = requests.get(url)
        image = Image.open(BytesIO(req.content))
        return image

img_dwnloader = ImageryDownloader(apiKey_MapBox)
img_dwnloader.download_tile(2,2,3)
'''



#HoughLines for edges
#'''
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
#'''







#loop through a bunch of gradient levels for an image in the same local directory - BROKEN???
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(manyBuildingPic,0)
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

im = cv.imread(manyBuildingPic)
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


#BROKEN - to similate a slider with keyboard input
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
