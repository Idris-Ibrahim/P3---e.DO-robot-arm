import cv2
from cv2 import aruco
import numpy as np
from object_detector import *

# Calibrate camera
calib_data_path = "D:/3/P3/P3-e.DO-robot-arm/MultiMatrix.npz"
calib_data = np.load(calib_data_path)
print(calib_data.files)
cam_mat = calib_data["camMatrix"]
dist_coef = calib_data["distCoef"]
r_vectors = calib_data["rVector"]
t_vectors = calib_data["tVector"]

MARKER_SIZE = 1.3  # centimeters



# Load Aruco detector
marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
param_markers = aruco.DetectorParameters_create()

# to end
i = 0

# Load Object Detector
detector = HomogeneousBgDetector()

# Load Cap
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Id distance list
alld10 =[]
alld11 =[]

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    i += 1

## kamera 1
    # Get Aruco marker
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners, _, _ = cv2.aruco.detectMarkers(frame, marker_dict, parameters=param_markers)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)
    
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners, MARKER_SIZE, cam_mat, dist_coef)
        total_markers = range(0, marker_IDs.size)

        # Draw polygon around the marker
        for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
            cv2.polylines(frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA)
            
        # Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners[0], True)
        
        
        # Pixel to cm ratio
        pixel_cm_ratio = aruco_perimeter / 5

        # distance
        distance = np.sqrt(tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2)

        contours = detector.detect_objects(frame)

        

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

            #cv2.drawFrameAxes(frame, cam_mat, dist_coef, rVec[i], tVec[i], 4, 4)
            cv2.putText(frame, f"id: {ids[0]} Dist: {round(distance, 1)}", (int(x - 100), int(y - 30)),cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(frame, [box], True, (255, 0, 0), 5)
            cv2.putText(frame, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(frame, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        
                 
        
        
        print("Width: ", object_width, "Length: ", object_height)    
    cv2.imshow("Image", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

    if i == 10000:
        exit()

cap.release()
cv2.destroyAllWindows()