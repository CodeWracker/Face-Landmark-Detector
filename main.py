from FaceMeshModule import FaceMeshDetector
import cv2
import time
from pprint import pprint

def main():
    cap = cv2.VideoCapture("./videos/eu3.mp4")
    vfps = (cap.get(cv2.CAP_PROP_FPS))
    detector = FaceMeshDetector(maxNumFaces=1,minDetectionConfidence=0.9    )
    pTime = 0
    FPS_MED = 0
    FPS = 0
    count_med = 0
    while True:
        success, img = cap.read()
        if(success):
            #print(success)
            img,faces = detector.findFaceMesh(img,False)
            #print(len(faces))
            for face in faces:
                print(face[4][2],30*(-face[4][2]),-500*(-face[4][2]))
                cv2.putText(img,"NOSE",(int(face[4][0]-500*(-face[4][2])),face[4][1]),cv2.FONT_HERSHEY_PLAIN,
            30*(-face[4][2]),(0,255,0),2)
            cTime = time.time()
            while 1/(cTime - pTime) > vfps:
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
        else:
            print("End of Video")
            break

if __name__ == "__main__":
    main()