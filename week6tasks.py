import numpy as np
import matplotlib.pyplot as plt

def my_spatial_filter(my_image_name, mask_size, filter_type):
#This is a simple function for calculating a spatial filter on an image, here we will start with a simple mean filter.
#Parameters:
#- my_image_name: Path to a grayscale image.
#Returns:
#- my_filtered_image: Resultant filtered image.

# Read the image
    I = plt.imread(my_image_name)
    # If the image is RGB, convert it to grayscale
    if I.ndim == 3:
        I = np.mean(I, -1)

    # Show the original image
    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.show()

    # make sure mask size is an odd number
    if mask_size % 2 == 0:
        pad = mask_size + 1
    else:
        pad = mask_size
    # Padding size
    padd_size = pad // 2
    # Pad the image with zeros
    I_padded = np.pad(I, ((padd_size, padd_size), (padd_size, padd_size)), mode='constant')
    # Show the padded image
    plt.imshow(I_padded, cmap='gray')
    plt.title('Padded Image')
    plt.show()

    # Create an output array for the filtered image data
    I2 = np.zeros_like(I_padded)
    # Loop through the image using nested loops extracting the pixel region
    for i in range(padd_size, I_padded.shape[0]-padd_size):
        for j in range(padd_size, I_padded.shape[1]-padd_size):
            pixbuffer = I_padded[i-padd_size:i+padd_size+1, j-padd_size:j+padd_size+1]
            if filter_type == 'mean':
                I2[i, j] = np.mean(pixbuffer)
            elif filter_type == 'median':
                I2[i, j] = np.median(pixbuffer)
            elif filter_type == 'min':
                I2[i, j] = np.min(pixbuffer)
            elif filter_type == 'max':
                I2[i, j] = np.max(pixbuffer)
            elif filter_type == 'range':
                min = np.min(pixbuffer)
                max = np.max(pixbuffer)
                I2[i, j] = max - min
            else:
                raise ValueError('Not a valid filter type.')
    # Extract the valid region from the filtered image
    my_filtered_image = I2[padd_size:-padd_size, padd_size:-padd_size]
    # Display the filtered image
    plt.imshow(my_filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.show()
    return my_filtered_image

my_spatial_filter('spnoise.png', 8, 'yes')