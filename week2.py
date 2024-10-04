import cv2
import matplotlib.pyplot as plt 
import numpy as np

image = cv2.imread('mario.jpg')
print(np.shape(image))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', gray_image)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Access a single pixel
pixel_value = image[50, 50]
# Access a row
row_values = image[50, :]
# Access a channel
red_channel = image[:, :, 0]

# Increase the intensity of the red channel by 50
image[:, :, 0] += 50


plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(binary_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Thresholded Image')
plt.show()
