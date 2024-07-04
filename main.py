import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# create a named window for video displayed
winName = "Traffic Signal Analysis"
cv.namedWindow(winName)

# Path of the video
path = "/Users/gauravsingh/Desktop/AI ENGINEER/Traffic Signal Detection/Video Traffic Light Sequence.mp4"

# Create a video capture object
video = cv.VideoCapture(path)

# Frame Count
frameCount = 0

# Light Status
lightStatus = "Unkown"

# Parameters for adding the text on image
font_face = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1.2
font_thickness = 1
font_color = (0,0,0)


# Enter the while loop to read and display video frame one by one.
while True:

    # Counting number of frames
    frameCount += 1

    # Use video capture object to read frame one at a time.
    has_frame, frame = video.read()
        
    # Break the loop if there is no video/ frame to display
    if not has_frame:
        print("No video frame to display.")
        break

    # Create a mask by using the first frame.
    # I have Used this mask to analys the colour pixels
    if frameCount == 1:
        mask = np.zeros_like(frame)
        mask[56:254, 146:200] = 255

    # Create a frame by masking all the surrounding near traffic light
    frameMasked = cv.bitwise_and(frame, frame, mask = mask[:,:,0])

    
    # After frame 120 the traffic light appears in the video hence used if condition.
    # Counting the number of array which has value 255.
    
    if frameCount >= 80:
        if np.sum(np.array(frameMasked[:,:,1]) == 255) >= 5:
            lightStatus = "Green"
            font_color = (0, 255, 0)

        elif np.sum(np.array(frameMasked[:,:,2]) == 255) >= 5:
            lightStatus = "Red"
            font_color = (0, 0, 255)

    # Adding text to the frame to display the traffic light detected.
    frame = cv.putText(frame, f"Traffic Light: {lightStatus}", (165, 50), font_face, font_scale, font_color, 1, cv.LINE_AA)
 
    # Display the video frame
    cv.imshow(winName, frame)

    # Use the waitKey function to monitor user input.
    key = cv.waitKey(1)

    if key == 'Q' or key == 'q' or key == 27:
        print("Video Stopped by user.")
        break

# Delete the video object and window
video.release()
cv.destroyAllWindows()
