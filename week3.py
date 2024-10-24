import cv2
import matplotlib.pyplot as plt 
import numpy as np

#Read the grayscale image
image = cv2.imread('lena.tiff')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Calculate histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

#Generate X values (0-255 for grayscale)
x_values = np.arange(256)

plt.bar(x_values, hist.ravel(), color='gray')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel values")
plt.ylabel("Frequency")
plt.show()

#Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Calculate histograms for each channel
hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])

#Generate X values (0-255 for each channel)
x_values = np.arange(256)

#Plot the histograms
plt.figure()
plt.bar(x_values, hist.ravel(), color='red', alpha=0.5, label='Red channel')
plt.bar(x_values, hist.ravel(), color='green', alpha=0.5, label='Green channel')
plt.bar(x_values, hist.ravel(), color='blue', alpha=0.5, label='Blue channel')
plt.title("RGB Histogram")
plt.xlabel("Pixel value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

#Subplot with all 4 histograms
plt.subplot(2, 2, 1)
plt.bar(x_values, hist.ravel(), color='red', alpha=0.5, label='Red channel')
plt.title('Red histogram')

plt.subplot(2, 2, 2)
plt.bar(x_values, hist.ravel(), color='green', alpha=0.5, label='Green channel')
plt.title('Green Histogram')

plt.subplot(2, 2, 3)
plt.bar(x_values, hist.ravel(), color='blue', alpha=0.5, label='Blue channel')
plt.title('Blue Histogram')

plt.subplot(2, 2, 4)
plt.bar(x_values, hist.ravel(), color='gray')
plt.title('Greyscale Histogram')
plt.show()

#DIY Histogram
def grayscale_histogram(image):
    hist = np.zeros(256, dtype=int)
    for pixel in image.ravel():
        hist[pixel]+= 1
    return hist

hist = grayscale_histogram(gray_image)
plt.plot(hist)
plt.show()

#histogram equalisation using built-in function
equalised_image = cv2.equalizeHist(gray_image)
plt.imshow(cv2.cvtColor(equalised_image, cv2.COLOR_BGR2RGB))
plt.show()

#Pout image and histogram
pout = cv2.imread('pout.tif')
gray_pout = cv2.cvtColor(pout, cv2.COLOR_BGR2GRAY)
hist_pout = cv2.calcHist([pout], [0], None, [256], [0, 256])
#Subplot with all image and histogram
plt.subplot(1, 2, 1)
plt.bar(x_values, hist_pout.ravel(), color='gray', alpha=0.5, label='Histogram')
plt.title('histogram')

plt.subplot(1, 2, 2)
plt.imshow(pout)
plt.title('Image')
plt.show()

#Equalised pout and histogram
equalised_pout = cv2.equalizeHist(gray_pout)
hist_eqpout = cv2.calcHist([equalised_pout], [0], None, [256], [0, 256])
plt.subplot(1, 2, 1)
plt.bar(x_values, hist_eqpout.ravel(), color='gray', alpha=0.5, label='Histogram Eq')
plt.title('histogram eq')

plt.subplot(1, 2, 2)
plt.imshow(equalised_pout)
plt.title('Image eq')
plt.show()

#built-in normalisation
normalised_pout = cv2.normalize(gray_pout, None, 0, 255, cv2.NORM_MINMAX)
plt.imshow(cv2.cvtColor(normalised_pout, cv2.COLOR_BGR2RGB))
plt.show()