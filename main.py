from FaceMeshModule import FaceMeshDetector
import cv2
import time
from pprint import pprint

def main():
    cap = cv2.VideoCapture("./videos/eu.mp4")
    detector = FaceMeshDetector(maxNumFaces=1,minDetectionConfidence=0.9    )
    pTime = 0
    FPS_MED = 0
    FPS = 0
    count_med = 0
    while True:
        try:
            success, img = cap.read()

            img,faces = detector.findFaceMesh(img)
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

if __name__ == "__main__":
    main()