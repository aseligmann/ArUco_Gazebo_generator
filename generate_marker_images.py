import numpy as np
import cv2
import cv2.aruco as aruco

# Select type of aruco marker (size)
aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)

# Create an image from the marker
size = 170 # 170px x 170px
for id in range(0, 250):
	img = aruco.drawMarker(aruco_dict, id, size)
	cv2.imwrite("markers/aruco_marker_" + str(id) + ".png", img)

