import cv2
p=r'C:\Users\HP\Downloads\WhatsApp Image 2023-10-16 at 8.26.58 AM.jpeg'
a=cv2.imread(p)
c=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("swetha",c)

