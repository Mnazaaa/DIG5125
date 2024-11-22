import cv2

# Create a VideoCapture object
cap = cv2 . VideoCapture ('Video1.avi')

# Check if camera opened successfully
if not cap.isOpened () :
    print (" Error : Could not open video .")
    exit ()

while cap.isOpened () :
# Capture frame -by - frame 
    ret, frame = cap.read ()
    if ret :
# Display the resulting frame
        cv2.imshow ('5', frame )

# Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord ('q'):
            break
        else :
            break

# When everything done , release the video capture object
cap.release ()
# Closes all the frames
cv2.destroyAllWindows ()



# Start video capture , ’0 ’ is the default webcam
cap = cv2.VideoCapture (0)

# Check if the webcam is opened correctly
if not cap.isOpened () :
    raise IOError (" Cannot open webcam ")

while True :
    ret , frame = cap.read ()
    if not ret:
        break

# Display the resulting frame
    cv2.imshow ('Webcam Live', frame )

# Break the loop when ’q’ is pressed
    if cv2.waitKey (1) & 0xFF == ord ('q') :
        break

# When everything is done , release the capture
cap.release ()
cv2.destroyAllWindows ()


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc (*'XVID')
out = cv2.VideoWriter ('output.avi', fourcc , 20.0 , (640 ,480))

# Open the camera
cap = cv2.VideoCapture (0)

while cap.isOpened () :
    ret, frame = cap.read ()
    if ret :
# Write the frame into the file ’output .avi ’
        out.write (frame)
        # Display the resulting frame
        cv2.imshow ('frame', frame)

# Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord ('q') :
            break
    else :
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


# Create a VideoCapture object
cap = cv2.VideoCapture ('Video1.avi')

# Check if video opened successfully
if not cap.isOpened () :
    print ("Error : Could not open video.")
    exit ()

# Get video properties
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get (cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
codec_code = int(cap.get(cv2.CAP_PROP_FOURCC))
codec = "". join ([chr(( codec_code >> 8 * i ) & 0xFF) for i in range(4)])

# Print video specifications

print ( f" Width : { width }")
print ( f" Height : { height }")
print ( f"FPS: {fps}")
print ( f" Number of frames : { frame_count }")
print ( f" Codec : { codec }")

# Release the video capture object
cap.release ()