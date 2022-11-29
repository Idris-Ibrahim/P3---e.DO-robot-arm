import cv2
from object_detector import *
import numpy as np
import pyrealsense2

# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

i = 0

# Load Object Detector
detector = HomogeneousBgDetector()

# Load Cap
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap2 = cv2.VideoCapture(4)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, img = cap.read()
    _, img2 = cap2.read()

    i += 1

## kamera 1
    # Get Aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    if corners:

        # Draw polygon around the marker
        int_corners = np.int0(corners)
        cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

        # Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners[0], True)
        

        # Pixel to cm ratio
        pixel_cm_ratio = aruco_perimeter / 20
        
        contours = detector.detect_objects(img)

        # Draw objects boundaries
        for cnt in contours:
            # Get rect
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect

            # Get Width and Height of the Objects by applying the Ratio pixel to cm
            object_width = w / pixel_cm_ratio
            object_height = h / pixel_cm_ratio

            # Display rectangle
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [box], True, (255, 0, 0), 2)
            cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            
## Kamera 2.
   # Get Aruco marker
    corners2, _, _ = cv2.aruco.detectMarkers(img2, aruco_dict, parameters=parameters)
    if corners2:

        # Draw polygon around the marker
        int_corners = np.int0(corners2)
        cv2.polylines(img2, int_corners, True, (0, 255, 0), 5)

        # Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners2[0], True)

        # Pixel to cm ratio
        pixel_cm_ratio = aruco_perimeter / 20

        contours = detector.detect_objects(img2)

        # Draw objects boundaries
        for cnt in contours:
            # Get rect
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect

            # Get Width and Height of the Objects by applying the Ratio pixel to cm
            object_width = w / pixel_cm_ratio
            object_height = h / pixel_cm_ratio

            # Display rectangle
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            cv2.circle(img2, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img2, [box], True, (255, 0, 0), 2)
            cv2.putText(img2, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img2, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    
    cv2.imshow("Image", img)
    cv2.imshow("Image2", img2)
    key = cv2.waitKey(1)
    if key == 27:
        break

    if i == 100:
        exit()

cap.release()
cap2.release()
cv2.destroyAllWindows()