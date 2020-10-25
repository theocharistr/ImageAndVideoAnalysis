import cv2
import numpy as np
import os

def Histogram(img):
    histogram = np.zeros(256)
    for k in range(256):
        histogram[k] = np.count_nonzero(k == img)
    return histogram / np.sum(histogram)


def otsu(img):
    myimg = Histogram(img)
    threshold = (-1, -1)  # best threshold
    for t in range(256):
        q1 = myimg[:t + 1].sum() + 1e-10
        m1 = 1 / q1 * (range(t + 1) * myimg[:t + 1]).sum()
        m2 = 1 / (1 - q1) * (range(t + 1, 256) * myimg[t + 1:]).sum()
        sigmaB = q1 * (1 - q1) * (m1 - m2) ** 2
        if sigmaB > threshold[1]:
            threshold = (t, sigmaB)
    final = np.zeros_like(img)
    print(img.shape)
    final[img >= threshold[0]] = 255
    return threshold[0], final

# Provide the path to loop throught the images

directory = r'C:\Users\haris\Desktop\IVA_TASK2\Input'

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        image_path = filename
        # print(image_path)
        new_path = os.path.splitext(image_path)[0]
        # print(new_path)

        img = cv2.imread('Input\{}'.format(image_path), cv2.IMREAD_GRAYSCALE)

        # img = cv2.imread('Input\finger.png', cv2.IMREAD_GRAYSCALE)

        # img = cv2.imread('Input\aluminium.png', cv2.IMREAD_GRAYSCALE)

        # img = cv2.imread('Input\phobos.png', cv2.IMREAD_GRAYSCALE)

        # img = cv2.imread('Input\julia.png', cv2.IMREAD_GRAYSCALE)

        cv2.imshow('Original Image', img)
        cv2.waitKey(0)

        t, newimg = otsu(img)
        print('Thresholded value:', t)
        cv2.imshow('{}Threshold{}.png'.format(new_path, t), newimg)
        k = cv2.waitKey(0)

        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'):  # wait for 's' key to save and exit
            cv2.imwrite('Output/{}Threshold{}.png'.format(new_path, t), newimg)
            cv2.destroyAllWindows()
