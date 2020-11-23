import cv2
import numpy as np
import os
""""
def convolution(img, filter):
    y, x = img.shape
    new_image = np.zeros((y, x))
    y = y - 3
    x = x - 3
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(img[i:i + 3, j:j + 3] * filter)
    return new_image.astype(np.uint8)
"""

filename = 'C:/Users/haris/Desktop/doc_db/pythonProject/3_noise.png'
imgColor = img = cv2.imread(filename, cv2.IMREAD_COLOR)
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(img.shape)

# show the original image

# print(img.shape)
# print the original full res image
cv2.namedWindow('original image')  # create window
cv2.imshow('original image', img)  # show image
cv2.waitKey(0)

# filter the noise (mainly salt and pepper but any other noise as well)
filter = 1 / 9 * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
imgFilter = cv2.filter2D(img, cv2.CV_8UC1, filter)
#imgFilter = convolution(img, filter)

# show filtered
imgFilterPrint = cv2.resize(imgFilter, (1000, 900))
cv2.imshow('after filter', imgFilterPrint)
cv2.waitKey(0)

# apply threshold in order to make the letters more distinct (black/white diff)
_, imgThresh = cv2.threshold(imgFilter, 150, 255, cv2.THRESH_BINARY)
imgThresh = cv2.bitwise_not(imgThresh)

imgThreshPrint = cv2.resize(imgThresh, (1000, 900))
cv2.imshow('after threshold', imgThreshPrint)
cv2.waitKey(0)

# apply the dilation effect to connect the words into bigger chunks of text
# replaced erosion with dilation because of binary reverse -----removed
# update: using both erosion and dilation
# kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
imgDilate = cv2.dilate(imgThresh, kernel, iterations=26)

kernelWords = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
imgDilateWords = cv2.dilate(imgThresh, kernelWords, iterations=10)

imgDilatePrint = cv2.resize(imgDilateWords, (1000, 900))
cv2.imshow('dialation', imgDilatePrint)
cv2.waitKey(0)

""""
imgDilatePrint = cv2.resize(imgDilate, (1000, 900))
cv2.imshow('dialation', imgDilatePrint)
cv2.waitKey(0)
"""

""""
imgErode = cv2.erode(imgDilate, kernel, iterations=3)
imgErodePrint = cv2.resize(imgErode, (1000, 900))
cv2.imshow('erosion', imgErodePrint)
cv2.waitKey(0)
"""
# find contours
contours, _ = cv2.findContours(imgDilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# counter starting at 1 instead of 0 to avoid a "zero box"
counter = 1
for cnt in contours:
    # get info for contour
    # x, y coords
    # h=height
    # w=width
    x, y, w, h = cv2.boundingRect(cnt)
    if (w < 400 and h < 400) or (w > 2000 and h > 2000):
        continue
    imageBoundaries = cv2.rectangle(imgColor, (x, y), (x + w, y + h), (0, 0, 255), 2)
    imageBoundaries = cv2.putText(imgColor, str(counter), (x, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
    print('--- Region', counter, '---')
    print('x=', x, 'y=', y, 'h=', h, 'w=', w)

    # finds white pixels in an image
    # in this case, letters (the binary image is: black background, white letters)
    lettersPixels = cv2.countNonZero(imgThresh[x:x + w, y:y + h])
    print('the number of pixels of letters: ', lettersPixels)
    print('Bounding Box Area(px):', h * w)

    # print every step of boundary drawn
    imageBoundariesPrint = cv2.resize(imageBoundaries, (1920, 900))
    #cv2.imshow('rectangles', imageBoundariesPrint)
    #cv2.waitKey(0)

    # find words in subregion currently drawn
    numWords, _ = cv2.connectedComponents(imgDilateWords[x:x + w, y:y + h])
    print('Number of words in subregion:', numWords)

    # find the gray level mean
    grayLevel = img[x:x + w, y:y + h].sum() / (h * w)
    print('Mean gray-level value in bounding box:', grayLevel)

    counter = counter + 1

imageBoundariesPrint = cv2.resize(imageBoundaries, (1000, 900))
cv2.imshow('rectangles', imageBoundariesPrint)
cv2.waitKey(0)
cv2.imwrite('C:/Users/haris/Desktop/doc_db/pythonProject/result.png',imageBoundaries)