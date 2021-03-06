#
# Mini example to understand basics of pose estimation with OpenCV.
# Example based on the following blog post: https://www.pythonpool.com/opencv-solvepnp/
# Image credits: Photo by Tatiana Zanon on Unsplash
#

import cv2
import numpy as np

img = cv2.imread("./img/imagen_test.jpg")
size = img.shape

points_2D = np.array(
    [
        (418, 247),  # Nose tip
        (392, 329),  # Chin
        (353, 199),  # Left eye corner
        (434, 203),  # Right eye corner
        (348, 270),  # Left mouth 
        (414, 279)   # Right mouth 
    ], dtype="double")

points_3D = np.array([
        (0.0, 0.0, 0.0),            #Nose tip
        (0.0, -330.0, -65.0),       #Chin
        (-225.0, 170.0, -135.0),    #Left eye corner
        (225.0, 170.0, -135.0),     #Right eye corner 
        (-150.0, -150.0, -125.0),   #Left mouth
        (150.0, -150.0, -125.0)     #Right mouth 
    ])

dist_coeffs = np.zeros((4,1))

frame_height, frame_width, channels = (500, 750, 3)

# pseudo camera internals
focal_length = frame_width
center = (frame_width / 2, frame_height / 2)
camera_matrix = np.array(
    [[focal_length, 0, center[0]], [0, focal_length, center[1]], [0, 0, 1]],
    dtype="double",
)

success, rotation_vector, translation_vector = cv2.solvePnP(
        points_3D,
        points_2D,
        camera_matrix,
        dist_coeffs,
        flags=0
    ) 

nose_end_point2D, jacobian = cv2.projectPoints(
        np.array([(0.0, 0.0, 1000.0)]),
        rotation_vector,
        translation_vector,
        camera_matrix,
        dist_coeffs
    )

for p in points_2D:
  cv2.circle(img, (int(p[0]), int(p[1])), 3, (0,0,255), -1)

point1 = ( int(points_2D[0][0]), int(points_2D[0][1]))
 
point2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
 
cv2.line(img, point1, point2, (255,255,255), 2)
 
 
# Display image
cv2.imshow("imagen test", img)

# Wait for key to exit
cv2.waitKey(0)
