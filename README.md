# Image and Video Processing
-Task 1: Gradient Magnitude & Non-Max Suppression   
-Task 2: Threshold Algorithm Otsu   
-Task 3: Hough Transformation  
-Task 4: Optic Flow & Motion Tracking  
-Task 5: Image Segmentation

## Task 1: Gradient Magnitude & Non-Max Suppression
 It illlustrates the fundamental steps of edge detection using gradient magnitude calculation and non-maximum suppression, similar to the initial stages of the Canny edge detection algorithm but without advanced noise reduction and thresholding steps.

Gradient Magnitude:
The gradient magnitude detects edges by calculating the intensity change at each pixel, often using the Sobel operator to compute horizontal and vertical gradients and then combining them.

Non-Max Suppression:
Non-max suppression thins edges by keeping only the local maxima in the gradient direction, enhancing edge precision by reducing thickness.

## Task 2: Threshold Algorithm Otsu
 It performs Otsu's thresholding on multiple images, calculating the optimal threshold for binarization by maximizing the between-class variance, and applies it to convert grayscale images into binary images. 
 
Otsu's method is a global thresholding technique that automatically determines the optimal threshold value to separate the foreground and background. It does this by maximizing the between-class variance (variance between the pixel values of the two classes) while minimizing the within-class variance.

## Task 3: Hough Transformation
It detects circles in images using the Hough Transform by processing edge-detected images, calculating possible circle centers and radii, and highlighting detected circles. It allows user input for diameter ranges and displays or saves the results.

The Hough Transform is a feature extraction technique used in image analysis to detect geometric shapes like lines and circles. It works by transforming points from the image space to a parameter space and identifying intersections in this parameter space, which correspond to the desired shapes in the image.

## Task 4: Optic Flow & Motion Tracking
It processes video files to visualize optical flow and track motion. It computes dense optical flow using the Farneback method, tracks feature points with the Lucas-Kanade method, and visualizes motion by drawing vectors and paths on the frames. The results are displayed and saved as video files.

Optic Flow:
Optic flow represents the pattern of apparent motion of objects in a visual scene caused by the relative motion between an observer and the scene. It is used to estimate the velocity of moving objects or the camera by analyzing the change in pixel intensity over time.

Motion Tracking:
Motion tracking involves following the position of moving objects over time in a sequence of images. Techniques like the Lucas-Kanade method are used to estimate the motion by matching feature points across successive frames.

## Task 5: Image Segmentation
It processes a grayscale image to detect text regions by filtering noise, applying thresholding, and using dilation. It then finds contours, analyzes each region, and draws bounding boxes around detected text areas. Finally, it displays and saves the resulting image with annotated regions.

Image segmentation is the process of partitioning an image into multiple segments (regions) to simplify or change the representation of the image, making it more meaningful and easier to analyze. Common techniques include thresholding, clustering (e.g., K-means), region growing, and advanced methods like Deep Learning-based segmentation.
