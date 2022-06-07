
import cv2
import matplotlib.pyplot as plt
import numpy as np

def emboss(frame):
    Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    Emboss_Effect_Img = cv2.filter2D(src=frame, kernel=Emboss_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Emboss_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.show()

def sharpen(frame):
    Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    Sharpen_Effect_Img = cv2.filter2D(src=frame, kernel=Sharpen_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Sharpen_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.show()
    
def sepia(frame):
    Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    Sepia_Effect_Img = cv2.filter2D(src=frame, kernel=Sepia_Kernel, ddepth=-1)
    plt.figure(figsize=(8,8))
    plt.imshow(Sepia_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.show()

def blur(frame):
    Blur_Effect_Img = cv2.GaussianBlur(frame, (35, 35), 0)
    plt.figure(figsize=(8,8))
    plt.imshow(Blur_Effect_Img,cmap="gray")
    plt.axis("off")
    plt.show()

def openCam():
    cv2.namedWindow("CAMMER")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        cv2.imshow("CAMMER", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            print("LATER NERD")
            break
        elif key == 49 or key == 97: # exit on ESC
            emboss(frame)
        elif key == 50 or key == 98: # exit on ESC
            sharpen(frame)
        elif key == 51 or key == 99: # exit on ESC
            sepia(frame)
        elif key == 52 or key == 100:
            blur(frame)
    
    vc.release()
    cv2.destroyWindow("CAMMER")
    
try:
    openCam()
except KeyboardInterrupt:
    print("LATER NERD")
