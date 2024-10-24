import cv2
import matplotlib.pyplot as plt 
import numpy as np

#Read the grayscale image
image = cv2.imread('lena.tiff')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Calculate histogram
hist = cv2.calcHist([gray_image], [0], None, [128], [0, 256])

#Generate X values (0-255 for grayscale)
x_values = np.arange(128)

plt.bar(x_values, hist.ravel(), color='gray')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel values")
plt.ylabel("Frequency")
plt.show()