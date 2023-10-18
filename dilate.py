import cv2
from numpy import*
k=ones((5,5),uint8)
p=r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg'
a=cv2.imread(p)
a1=cv2.resize(a,(200,200))
v3=cv2.dilate(a1,k,3)
cv2.imshow("swe_bef",a1)
cv2.imshow("swe_af",v3)
