## Image-and-Video-Processing
-Task 1: Gradient Magnitude & Non-Max Suppression   
-Task 2: Threshold Algorithm Otsu   
-Task 3: Hough Transformation  
-Task 4: Optic Flow & Motion Tracking  
-Task 5: Image Segmentation

Task 1: Gradient Magnitude & Non-Max Suppression
Gradient Magnitude:
The gradient magnitude of an image is used to detect edges by calculating the change in intensity at each pixel. This is typically done using the Sobel operator, which computes the gradients in the horizontal and vertical directions, and then combines them to get the gradient magnitude.

Non-Max Suppression:
After computing the gradient magnitude, non-max suppression is applied to thin the edges. This process retains only the local maxima in the direction of the gradient, effectively reducing the thickness of edges and making them more precise.

Task 2: Threshold Algorithm Otsu
Otsu's method is a global thresholding technique that automatically determines the optimal threshold value to separate the foreground and background. It does this by maximizing the between-class variance (variance between the pixel values of the two classes) while minimizing the within-class variance.

Task 3: Hough Transformation
The Hough Transform is a feature extraction technique used in image analysis to detect geometric shapes like lines and circles. It works by transforming points from the image space to a parameter space and identifying intersections in this parameter space, which correspond to the desired shapes in the image.

Task 4: Optic Flow & Motion Tracking
Optic Flow:
Optic flow represents the pattern of apparent motion of objects in a visual scene caused by the relative motion between an observer and the scene. It is used to estimate the velocity of moving objects or the camera by analyzing the change in pixel intensity over time.

Motion Tracking:
Motion tracking involves following the position of moving objects over time in a sequence of images. Techniques like the Lucas-Kanade method are used to estimate the motion by matching feature points across successive frames.

Task 5: Image Segmentation
Image segmentation is the process of partitioning an image into multiple segments (regions) to simplify or change the representation of the image, making it more meaningful and easier to analyze. Common techniques include thresholding, clustering (e.g., K-means), region growing, and advanced methods like Deep Learning-based segmentation.
