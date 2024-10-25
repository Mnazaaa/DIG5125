import cv2
from scipy.signal import convolve2d
import numpy as np

def simple_1d_convolution(input_array, conv_mask):
#Perform 1D convolution on an input array using a convolution mask.
#Parameters:
#input_array (list or np.array): The input numbers array.
#conv_mask (list or np.array): The convolution mask.
#Returns:
#np.array: The convolution result.
    return np.convolve(input_array, conv_mask, mode='full')

def simple_2d_convolution(input_array, conv_mask):
#Perform 2D convolution on an input array using a convolution mask.
#Parameters:
#input_array (np.array): The 2D input array.
#conv_mask (np.array): The convolution mask.
#Returns:
#np.array: The convolution result.
    return convolve2d(input_array, conv_mask, mode='full')

input_array = np.array([1, 2, 3, 4, 5, 6])
conv_mask = np.array([1, 1, 1, 1, 1])
convolution_result = simple_1d_convolution(input_array, conv_mask)
print("Convolution Result:", convolution_result)

input_array2 = np.array([[1,2,3,2],[2,1,1,2],[50,55,50, 55],[55,50,50,55]])
conv_mask2 = np.array([[1,1,1], [0, 0, 0], [-1,-1,-1]])
convolution_result2 = simple_2d_convolution(input_array2, conv_mask2)
print("2D Convolution Result:", convolution_result2)

def my_loop_convolution(my_input_array, my_conv_mask):
#Perform 1D convolution on an input array using a convolution mask with loops.
#Parameters:
#my_input_array (list or np.array): The input numbers array.
#my_conv_mask (list or np.array): The convolution mask.
#Returns:
#np.array: The convolution result.
# Ensure the input arrays are numpy arrays
    my_input_array = np.array(my_input_array)
    my_conv_mask = np.array(my_conv_mask)
    # Initialize an empty array with the same length as the input array
    my_result = np.zeros(len(my_input_array) + len(my_conv_mask) - 1)
    # Loop through the data in the arrays
    for i in range(len(my_input_array)):
        for j in range(len(my_conv_mask)):
            # Ensure we do not go out of array bounds
            if i + j < len(my_result):
                my_result[i + j] += my_input_array[i] * my_conv_mask[j]
            # Display the results
            print("Convolution Result:", my_result)
            return my_result
        

def apply_averaging_blur(image_path, kernel_size):
#Apply an averaging blur using a specific kernel size.
#Parameters:
#image_path (str): Path to the image file.
#kernel_size (int): Size of the averaging kernel. Must be odd.
    image = cv2.imread(image_path)
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    cv2.imshow("Original", image)
    cv2.imshow("Averaging Blur", blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

apply_averaging_blur('mario.jpg', 5)