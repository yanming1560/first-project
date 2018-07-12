import cv2
import random
import numpy as np
cap=cv2.VideoCapture(0)
x=random.randint(0,320)
y=random.randint(0,240)
r=random.randint(1,5)
i=0
black1=np.array([211,211,211])
black2=np.array([255,255,255])
while(1):
    ret, frame= cap.read()
    #if i>0:
        #vars()['fr' + str(i)]=cv2.addWeighted(vars()['fr'+str(i)], 0.1, vars()['fr'+str(i-1)], 0.91, 0)
    x=x+random.randint(-10,10)
    y=y+random.randint(-10,10)
    r=r+random.randint(-4,4)
    #cv2.circle(vars()['fr' + str(i)], (x,y ), abs(r),(random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1)
    cv2.imshow("capture", frame)
    i += 1
    mask = cv2.inRange(frame, black1,black2)
    cv2.imshow("result",mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
