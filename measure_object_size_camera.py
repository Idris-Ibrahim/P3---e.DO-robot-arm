import cv2
from object_detector import *
import numpy as np
from cv2 import aruco

# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# Calibrate camera
calib_data_path = "MultiMatrix.npz"
calib_data = np.load(calib_data_path)
print(calib_data.files)
cam_mat = calib_data["camMatrix"]
dist_coef = calib_data["distCoef"]

# Load Object Detector
detector = HomogeneousBgDetector()

MARKER_SIZE = 3  # centimeters

alld10 =[]
alld11 =[]
Width = []
Length = []
Height = []

# Load Cap
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
counter = 0

object_width = float(0)
        
object_length = float(0)

avg10 = []
avg11 = []

while counter <= 20:
    _, img = cap.read()
    counter += 1
    # Get Aruco marker
    corners, ids, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    if ids is not None and ids[0] == 10:
        # Draw polygon around the marker
        int_corners = np.int0(corners)
        cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

        # Aruco Perimeter
        aruco_perimeter = cv2.arcLength(corners[0], True)

        # Pixel to cm ratio
        pixel_cm_ratio = aruco_perimeter / 10

        contours = detector.detect_objects(img)
        
        # Draw objects boundaries
        for cnt in contours:
            # Get rect
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect

            # Get Width and Height of the Objects by applying the Ratio pixel to cm
            object_width = w / pixel_cm_ratio
            object_length = h / pixel_cm_ratio

            # Display rectangle
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [box], True, (255, 0, 0), 2)
            cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(img, "Length {} cm".format(round(object_length, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            
            if object_width > 7:
                Width.append(object_width)
            if object_length > 7:
                Length.append(object_length)

        #print("Width: ", object_width, "Length: ", object_length)
         
    if cv2.waitKey(27) & 0xFF == ord("q"):
        break

        

    if counter >= 75:
        break
counter = 0
while counter <= 20:
    counter += 1
    ret, frame = cap.read()
    if not ret:
        break  
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = cv2.aruco.detectMarkers(gray_frame, aruco_dict, parameters=parameters)
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners, MARKER_SIZE, cam_mat, dist_coef)
        total_markers = range(0, marker_IDs.size)
        for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
            cv2.polylines(
                frame, [corners.astype(np.int32)], True, (0, 0, 255), 4, cv2.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()

            # Since there was mistake in calculating the distance approach point-outed in the Video Tutorial's comment
            # so I have rectified that mistake, I have test that out it increase the accuracy overall.
            # Calculating the distance
            distance = np.sqrt(
                tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
            )
            
            # Draw the pose of the marker
            cv2.putText(frame,f"id: {ids[0]} Dist: {round(distance, 2)}",top_right,cv2.FONT_HERSHEY_PLAIN,1.3,(0, 0, 255),2,cv2.LINE_AA,)
            
            
            if (ids == [10]):
                #print(ids, distance)
                alld10.append(distance)
                #print(alld10)
                #print("avarage distance for id 10 is: ", round(avg10,2))
        
            if (ids == [11]):
                #print(ids, distance)
                alld11.append(distance)
                #print(alld11)
                #print("avarage distance for id 11 is: ", round(avg11,2))
        
        avg10 = sum(alld10) / len(alld10)   
        avg11 = sum(alld11) / len(alld11)   
          
        Width.append(object_width)
        Length.append(object_length)
        final_width = sum(Width) / len(Width)
        final_length = sum(Length) / len(Length) 
        Hight = avg10 - avg11
        
        
        print("width: ", final_width, "Length: ", final_length,"Height: ",Hight)
    cv2.imshow("Width & lenght", img)
    cv2.imshow("Hight", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break    
cap.release()
cv2.destroyAllWindows()

WidthAvg = sum(Width)/len(Width)
LengthAvg = sum(Length)/len(Length)


Measurement = [WidthAvg, LengthAvg, Hight]

# open a file for writing
with open('3dbinpacking-master/Measurements.txt', 'a') as f:
    # write each number to the file, followed by a newline character
    f.write(str(Measurement[0]) + ',')
    f.write(str(Measurement[1]) + ',')
    f.write(str(Measurement[2]) + '\n')
