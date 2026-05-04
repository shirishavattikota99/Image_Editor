import cv2
import numpy as np

# 1. Blur
def Blur(img, ksize):
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(img, (ksize, ksize), 0)



# 2. Brightness
def Brightness(img, beta):
    return cv2.convertScaleAbs(img, alpha=1, beta=beta)


# 3. Contrast
def Contrast(img, alpha):
    return cv2.convertScaleAbs(img, alpha=alpha, beta=0)


# 4. Sharpness
def Sharpen(img, alpha):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(img, -1, kernel)
    return cv2.addWeighted(img, 1-alpha, sharp, alpha, 0)


# 5. Edge Detection
def Edge_Detection(img, t1, t2):
    return cv2.Canny(img, t1, t2)


# 6. Grayscale
def Grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
