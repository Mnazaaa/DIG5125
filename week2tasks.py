import cv2
import matplotlib.pyplot as plt 
import numpy as np

#TASK 1
def bin_gray(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('imageg', gray_image)
    cv2.imshow('imageb', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bin_gray(cv2.imread('mario.jpg'))

#TASK 2
image = cv2.imread('mario.jpg')
cv2.imshow('original', image)
# Increase the intensity of the blue channel by 50
image[:, :, 2] += 30
# Decrease the intensity of the green channel by 25
image[:, :, 1] += 60
cv2.imshow('modified', image)
cv2.waitKey(0)

#TASK 3
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh1 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
_,thresh2 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Thresholded Image1')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(thresh2, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Thresholded Image2')
plt.show()


#TASK 4
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
red_channel = RGB[:, :, 0]
green_channel = RGB[:, :, 1]
blue_channel = RGB[:, :, 2]
new = RGB.copy()
new[:,:,0]= blue_channel
new[:,:,2]= red_channel
cv2.imshow('original', RGB)
cv2.imshow('swapped', new)
cv2.waitKey(0)