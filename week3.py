import cv2
import matplotlib.pyplot as plt 
import numpy as np

#Read the grayscale image
image = cv2.imread('lena.tiff')

#Calculate histogram
hist = cv2.calcHist([image], 0, None, [256], [0, 256])

#Generate X values (0-255 for grayscale)
x_values = np.arange(256)

plt.bar(x_values, hist.ravel(), color='gray')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel value")
plt.ylabel("Frequency")
plt.show()