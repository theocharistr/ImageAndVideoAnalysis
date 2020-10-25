import cv2
import numpy as np


def convolution(img, filter):
    m, n = filter.shape
    if (m == n):
        y, x = img.shape
        new_image = np.zeros((y, x))
        y = y - m + 1
        x = x - m + 1
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(img[i:i + m, j:j + m] * filter)
    return new_image


def nonmax_suppression(img, theta):
    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = theta * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            try:
                q = 255
                r = 255

                # angle 0
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = img[i + 1, j]
                    r = img[i - 1, j]
                # angle 45
                elif (22.5 <= angle[i, j] < 67.5):
                    q = img[i - 1, j - 1]
                    r = img[i + 1, j + 1]
                # angle 90
                elif (67.5 <= angle[i, j] < 112.5):
                    q = img[i, j + 1]
                    r = img[i, j - 1]
                # angle 135
                elif (112.5 <= angle[i, j] < 157.5):
                    q = img[i + 1, j - 1]
                    r = img[i - 1, j + 1]

                if (img[i, j] >= q) and (img[i, j] >= r):
                    Z[i, j] = img[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    return Z


#Pick an image
img = cv2.imread('Input\julia.png', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('Input\motor.png', cv2.IMREAD_GRAYSCALE)
#img= cv2.imread('Input\circlegrey.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', img)
cv2.waitKey(0)


#Prewitt
Gx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

fx = convolution(img, Gx)/3
Gy = Gx.T
fy = convolution(img, Gy)/3

#Magnitude  M(x, y)
Magnitude= np.sqrt(np.power(fx, 2) + np.power(fy, 2))
# mapping values from 0 to 255

Result = ((Magnitude-np.min(Magnitude))/(np.max(Magnitude)-np.min(Magnitude)) * 255)

#orientation Θ(x, y)
theta = np.arctan2(fx, fy)


cv2.imshow('Gradient Magnitude', Result.astype(np.uint8))
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('Gradient Magnitude.png', Result.astype(np.uint8))
    cv2.destroyAllWindows()
print(Result)
print(theta)
Ms = nonmax_suppression(Result, theta)
print(Ms)
cv2.imshow('Non-Max Suppression', Ms.astype(np.uint8))
k = cv2.waitKey(0)

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('Non-Max Suppression_julia.png', Ms.astype(np.uint8))
    cv2.destroyAllWindows()
