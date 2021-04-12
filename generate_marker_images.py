import numpy as np
import cv2
import cv2.aruco as aruco

# Select type of aruco marker (size)
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)

# Create an image from the marker
size = 200 # 200px x 200px
for id in range(0, 250):
	img = aruco.drawMarker(aruco_dict, id, 200)
	cv2.imwrite("markers/aruco_marker_" + str(id) + ".png", img)

