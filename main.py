import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("./videos/eu.mp4")

pTime = 0
FPS_MED = 0
FPS = 0
count_med = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)

while True:
    try:
        success, img = cap.read()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACE_CONNECTIONS)
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        FPS+=fps
        count_med+=1
        if(count_med == 10):
            FPS_MED = FPS/10
            FPS = 0
            count_med = 0
        cv2.putText(img,f'FPS: {int(FPS_MED)}',(20,70),cv2.FONT_HERSHEY_PLAIN,
        3,(0,0,0),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    except cv2.error:
        print("End of Video")
        break
        