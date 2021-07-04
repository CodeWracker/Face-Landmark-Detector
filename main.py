from FaceMeshModule import FaceMeshDetector
import cv2
import os
from tqdm import tqdm

def detect_face_on_video(path):
    cap = cv2.VideoCapture( str(path))
    vfps = (cap.get(cv2.CAP_PROP_FPS))
    
    detector = FaceMeshDetector(maxNumFaces=2,minDetectionConfidence=0.9)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    name = path.split('/')
    name = name[len(name)-1].split('.')
    name = name[0]
    name =  './videos/lms/'+name + '.avi'
    (h,w) = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(name, fourcc,int(vfps),(h,w))


    while True:
        success, img = cap.read()
        if(success):
            #print(success)
            img2,faces = detector.findFaceMesh(img,True)
            
            
            img2 = cv2.resize(img2, (h,w))
            
            out.write(img2)
        else:
            print("End of Video")
            break
    cap.release()
    cv2.destroyAllWindows()
    out.release()

if __name__ == "__main__":
    for video in tqdm(os.listdir('./videos/raw')):
        detect_face_on_video("./videos/raw/"+video)