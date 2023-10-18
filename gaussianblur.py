import cv2
p=r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg'
a=cv2.imread(p)
a1=cv2.resize(a,(600,600))
c=cv2.GaussianBlur(a1,(5,5),10)
cv2.imshow("swe_bef",a1)
cv2.imshow("swe_af",c)
