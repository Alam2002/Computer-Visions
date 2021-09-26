import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture("run.mp4")

pTime = 0

while True:
    success, img = capture.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)


    cv2.imshow("Video",img)
    cv2.waitKey(10)