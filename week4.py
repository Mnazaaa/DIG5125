import cv2
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import numpy as np

#Load the image using OpenCV
ImageA = cv2.imread('mario.jpg', cv2.IMREAD_UNCHANGED)
ImageB = cv2.imread('mandrill.jpg', cv2.IMREAD_UNCHANGED)

#Check the dimensions of ImageA and convert if needed
def image_type(ImageA):
    if ImageA is None:
        print("Error: Could not read the image.")
        exit()

    dims = np.shape(ImageA)

    if len(dims) == 3 and dims[2] == 3: #RGB image
        Imagea1 = cv2.cvtColor(ImageA, cv2.COLOR_BGR2GRAY)
        print('Image A is an RGB image, it is now converted to grayscale')

    #Check for images with channels > 3
    elif len(dims) == 3 and dims[2] > 3:
        print('Image A is not an RGB image')
        exit()
    else: #Grayscale image
        print('Image A is a grayscale image, no conversion needed')

#Load RGB images
ImageA_RGB = cv2.imread('mario.jpg', cv2.IMREAD_COLOR)
ImageB_RGB = cv2.imread('mandrill.jpg', cv2.IMREAD_COLOR)
#check if images were successfully loaded
if ImageA_RGB is None or ImageB_RGB is None:
    print("Error: Could not read one or both images.")
    exit()
#Convert RGB image to grayscale for further processing
ImageA1 = cv2.imread('mario.jpg', cv2.COLOR_BGR2GRAY)
ImageB1 = cv2.imread('mandrill.jpg', cv2.COLOR_BGR2GRAY)
#Get the sizes of the images
sizeA = ImageA1.shape
sizeB = ImageB1.shape
if sizeA != sizeB:
    #resize based on the dimensions pf ImageA1
    print("The images are different sizes. Resizing ImageB1 to match ImageA1.")
    ImageB1 = cv2. resize(ImageB1, (sizeA[1], sizeA[0]))
else:
    print("The images are the same size, therefore i can continue.")
#Threshold the grayscale images to create a binary result. 127 is the threshold value, you can adjust it if needed.
_, ImageA2 = cv2.threshold(ImageA1, 127, 255, cv2.THRESH_BINARY)
_, ImageB2 = cv2.threshold(ImageB1, 127, 255, cv2.THRESH_BINARY)

ImageC = cv2.bitwise_and(ImageA2, ImageB2)

fig = plt.figure()
gs = gridspec.GridSpec(2, 5, width_ratios=[1, 1, 1, 2, 2], height_ratios=[2,1])

ax1 = plt.subplot(gs[0])
ax1.imshow(cv2.cvtColor(ImageA, cv2.COLOR_BGR2RGB))
ax1.set_title('Original A')
ax1.axis('off')

ax2 = plt.subplot(gs[1])
ax2.imshow(ImageA1, cmap='gray')
ax2.set_title('grayscale')
ax2.axis('off')

ax3 = plt.subplot(gs[2])
ax3.imshow(ImageA2, cmap='gray')
ax3.set_title('Binary')
ax3.axis('off')

ax4 = plt.subplot(gs[5])
ax4.imshow(cv2.cvtColor(ImageB, cv2.COLOR_BGR2RGB))
ax4.set_title('Original B')
ax4.axis('off')

ax5 = plt.subplot(gs[6])
ax5.imshow(ImageB1, cmap='gray')
ax5.set_title('grayscale')
ax5.axis('off')

ax6 = plt.subplot(gs[7])
ax6.imshow(ImageB2, cmap='gray')
ax6.set_title('BW')
ax6.axis('off')

#spanning over multiple positions for the "And Image"
ax7 = plt.subplot(gs[3:5])
ax7.imshow(ImageC, cmap='gray')
ax7.set_title('And Image')
ax7.axis('off')

plt.tight_layout()
plt.show()

MyImageBW = np.copy(ImageA2)
#create the structuring element (disk with radius 5)
MyStrel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
#Dilation
MyDilation = cv2.dilate(MyImageBW, MyStrel, iterations=1)
#Erosion
MyErosion = cv2.erode(MyImageBW, MyStrel, iterations=1)
#Plotting the images
images = [cv2.cvtColor(ImageA, cv2.COLOR_BGR2RGB), MyImageBW, MyDilation, MyErosion, MyStrel]
titles = ['Original', 'BW Image', 'Dilation', 'Erosion', 'My strel']

plt.figure()

for i, (img, title) in enumerate(zip(images, titles), 1):
    plt.subplot(1,5,i)
    if i == 1: #if it is the original color image
        plt.imshow(img)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()