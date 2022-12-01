# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2
# np is an alias pointing to numpy library
import numpy as np


# capture frames from a camera
cap = cv2.VideoCapture(2)


# loop runs if capturing has been initialized
while(1):

	# reads frames from a camera
	ret, frame = cap.read()

	# converting BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	operatedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	corners = cv2.goodFeaturesToTrack(operatedImage,25,0.01,10)
	corners = np.int0(corners)
	# modify the data type
	# setting to 32-bit floating point
	operatedImage = np.float32(operatedImage)
	# apply the cv2.cornerHarris method

	# to detect the corners with appropriate
	# values as input parameters
	dest = cv2.cornerHarris(operatedImage, 2, 3, 0.01)
	# Results are marked through the dilated corners
	dest = cv2.dilate(dest, None)
	
	# Reverting back to the original image,
	# with optimal threshold value
	frame[dest > 0.01 * dest.max()]=[0, 0, 255]
	
	# the window showing output image with corners
	cv2.imshow('Image with Borders', frame)
	
	# define range of red color in HSV
	lower_red = np.array([30,150,50])
	upper_red = np.array([255,255,180])
	
	# create a red HSV colour boundary and
	# threshold HSV image
	mask = cv2.inRange(hsv, lower_red, upper_red)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	# Display an original image
	cv2.imshow('Original',frame)

	# finds edges in the input image and
	# marks them in the output map edges
	edges = cv2.Canny(frame,200,200)

	# Display edges in a frame
	cv2.imshow('Edges',edges)

	# Wait for Esc key to stop
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
