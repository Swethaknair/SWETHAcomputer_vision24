import cv2
import numpy as np
img=cv2.imread(r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg')
rows,cols,_= img.shape
M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('image',dst)
