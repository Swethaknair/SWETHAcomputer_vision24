import cv2
p=(r'C:\Users\HP\Downloads\WhatsApp Video 2023-10-16 at 9.36.47 AM.mp4')
c=cv2.VideoCapture(p)
i=0
while True:
    a,r=c.read()
    i+=1
    cv2.imshow("a",r1)
    if(i<300):
        cv2.waitkey(1)
    else:
        cv2.waitkey(250)
