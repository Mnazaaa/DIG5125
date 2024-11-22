import cv2
import numpy as np

# Open the video
video = cv2.VideoCapture(0)

while True :
    ret , frame = video.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Isolate the saturation channel and adjust the saturation
    h,s,v = cv2.split(hsv)
    s = cv2.multiply(s,1.2) # Increase saturation by 20%
    adjusted_hsv = cv2.merge([ h , s , v ])
    # Convert back to BGR
    adjusted_frame = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
    # Display the original and the adjusted frame
    combined_frame = np.hstack((frame,adjusted_frame))
    cv2.imshow('Original vs Adjusted', combined_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
