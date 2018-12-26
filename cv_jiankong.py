import cv2,numpy,time
cap=cv2.VideoCapture(0)
ret, frame= cap.read()
frame_old=cv2.GaussianBlur(frame,(21,21),0)
while(1):
    ret, frame= cap.read()
    frame=cv2.GaussianBlur(frame,(21,21),0)
    diff=cv2.absdiff(frame,frame_old)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    thresh=cv2.erode(thresh, (21, 21), iterations=1)
    thresh = cv2.dilate(thresh, (21, 21), iterations=1)
    # image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if numpy.any(thresh)==True:
        h, m, s = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
        print("%d:%d:%d,move"%(h,m,s))
    cv2.imshow("capture",frame)
    cv2.imshow('d',thresh)
    time.sleep(0.5)
    frame_old = frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
