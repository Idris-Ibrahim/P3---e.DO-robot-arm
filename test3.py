import cv2
import numpy as np

# Load the camera matrix and distortion coefficients
# Calibrate camera
calib_data_path = "D:/3/P3/P3-e.DO-robot-arm/MultiMatrix.npz"
calib_data = np.load(calib_data_path)
print(calib_data.files)
camera_matrix = calib_data["camMatrix"]
distortion_coefficients = calib_data["distCoef"]

# Load the size of the Aruco markers in meters
marker_size = 0.04 # 5 cm

# Load the positions of the markers in the object's coordinate system
# These values should be known a priori
marker_positions = np.array([[0, 0, 0],
                             [marker_size, 0, 0],
                             [marker_size, marker_size, 0],
                             [0, marker_size, 0],
                             [0, 0, marker_size],
                             [marker_size, 0, marker_size],
                             [marker_size, marker_size, marker_size],
                             [0, marker_size, marker_size]])

# Load the image of the object with the Aruco markers
# Load Cap
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
counter = 0

# Detect the Aruco markers in the image
marker_corners, marker_ids, _ = cv2.aruco.detectMarkers(cap, cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50))

# Estimate the pose of each marker
_, rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(marker_corners, marker_size, camera_matrix, distortion_coefficients)

# Convert the rotation vector to a rotation matrix
rotation_matrix, _ = cv2.Rodrigues(rvec)

# Convert the rotation matrix and translation vector to a 4x4 transformation matrix
transform_matrix = np.concatenate((rotation_matrix, tvec), axis=1)
transform_matrix = np.concatenate((transform_matrix, np.array([[0, 0, 0, 1]])), axis=0)

# Transform the marker positions from the object's coordinate system to the camera's coordinate system
marker_positions_camera = np.dot(transform_matrix, np.concatenate((marker_positions, np.ones((8, 1))), axis=1).T).T

# Compute the dimensions of the object in the camera's coordinate system
width = np.linalg.norm(marker_positions_camera[1] - marker_positions_camera[0])
length = np.linalg.norm(marker_positions_camera[2] - marker_positions_camera[1])
depth = np.linalg.norm(marker_positions_camera[4] - marker_positions_camera[0])

print('Width:', width)
print('Length:', length)
print('Depth:', depth)
cv2.imshow("cap", cap)