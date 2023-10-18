import cv2
import numpy as np
img1 = cv2.imread(r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg')
img2 = cv2.imread(r'C:\Users\HP\Pictures\Screenshots\Screenshot 2023-10-16 123250.png')
pts1 = np.array([[50, 50], [100, 50], [50, 100], [100, 100]])
pts2 = np.array([[100, 100], [200, 100], [100, 200], [200, 100]])
H, _ = cv2.findHomography(pts1, pts2)
dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

