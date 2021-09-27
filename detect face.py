import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture("war.mp4")# Here you can use any of your video in your directory
pTime = 0


mpFD = mp.solutions.face_detection
faceDetection = mpFD.FaceDetection()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id,detection in enumerate(results.detections):
            #mpDraw.draw_detection(img,detection)
            print(detection.location_data.relative_bounding_box)
            print(detection.score)
            bbxC = detection.location_data.relative_bounding_box

            ih, iw,ic = img.shape
            bbx = int(bbxC.xmin*iw),int(bbxC.ymin*ih), int(bbxC.width*iw),int(bbxC.height*ih)
            cv2.rectangle(img, bbx,(255, 0, 255), 2)
            cv2.putText(img,  str(int(detection.score[0]*100))+"%", (bbx[0], bbx[1]-30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,"fps: "+str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(0,255,0),2)


    cv2.imshow("Video",img)
    cv2.waitKey(1)