import cv2
import numpy as np
img = cv2.imread(r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg')
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.magnitude(dx, dy)
thresh = 100
edges[edges < thresh] = 0
edges[edges >= thresh] = 255
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
