import cv2
cap =cv2.VideoCapture(0); #default camera 1 0r -1 ,file name ,path

while(True):
    ret , frame  = cap.read()
    # color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
