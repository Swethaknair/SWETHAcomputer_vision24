import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread(r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(100,100))
cv2.imshow("image",img)
