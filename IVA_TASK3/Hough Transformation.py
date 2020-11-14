import numpy as np
import cv2
import os

def accumulator(img, DiameterRange):
    [d1, d2] = DiameterRange
    r1 = int(d1) // 2
    r2 = int(d2) // 2
    height, width = img.shape
    AccMatrix = np.zeros([height * 2, width * 2, r2 + 1])  # fill with zeroes initially, instantiate 3D matrix
    for r in range(r1, r2):
        for h in range(height):
            for w in range(width):
                if img[h][w] != 0:
                    for theta in range(0, 360):  # the possible  theta 0 to 360
                        b = w - r * np.sin(theta * np.pi / 180)  # polar coordinate for center(convert to radians)
                        a = h - r * np.cos(theta * np.pi / 180)  # polar coordinate for center(convert to radians)
                        AccMatrix[int(a), int(b), int(r)] += 1  # voting
    Acc = np.sum(AccMatrix, axis=2)  # Sum up the  axis with the radius
    Acc = ((Acc - Acc.min()) / (Acc.max() - Acc.min()) * 255)  # Normalization
    AccImg = Acc[:height + 1, :width + 1]
    indexes = np.argwhere(AccMatrix > 0.7 * np.max(AccMatrix))  # Set threshold for accepted values
    return indexes, AccImg


directory = r'C:\Users\haris\Desktop\IVP\IVA_TASK3\Input'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        image_path = filename
        # print(image_path)
        new_path = os.path.splitext(image_path)[0]
        # print(new_path)

        img = cv2.imread('Input\{}'.format(image_path))

        # img = cv2.imread('Input\finger.png')

        # img = cv2.imread('Input\aluminium.png')

        # img = cv2.imread('Input\phobos.png')

        # img = cv2.imread('Input\julia.png')

        cv2.imshow('Original Image', img)
        cv2.waitKey(0)
        GausImg = cv2.GaussianBlur(img, (3, 3), 0)  # Blur the image with Gaussian filter
        EdgeImg = cv2.Canny(GausImg, 50, 150)  # Apply Canny edge filter
        print('Provide range of diameters')
        d1, d2 = input().split()
        indexes, accumulator_img = accumulator(EdgeImg, [d1, d2])  # Hough Transform
        cv2.imshow('Accumulator Image', accumulator_img.astype(np.uint8))
        k = cv2.waitKey(0)
        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'):  # wait for 's' key to save and exit
            cv2.imwrite('Accumulator Image {}.png'.format(new_path), accumulator_img.astype(np.uint8))
            cv2.destroyAllWindows()

        for h, w, r in indexes:
            cv2.circle(img, (w, h), r, (0, 0, 255), thickness=1, lineType=8, shift=0)  #
        cv2.imshow('Circles Detected on Image', img)
        k = cv2.waitKey(0)
        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
        elif k == ord('s'):  # wait for 's' key to save and exit
            cv2.imwrite('Circles Detected on Image {} with diameters{},{}.png'.format(new_path, d1, d2), img)
            cv2.destroyAllWindows()
