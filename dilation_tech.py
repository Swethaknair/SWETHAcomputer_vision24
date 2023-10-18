import cv2
import numpy as np
img = cv2.imread(r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg')
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()






                            
