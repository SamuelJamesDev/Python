import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time

def emboss(frame):
    Emboss_Kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    Emboss_Effect_Img = cv2.filter2D(src=frame, kernel=Emboss_Kernel, ddepth=-1)
    return Emboss_Effect_Img

def sharpen(frame):
    Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    Sharpen_Effect_Img = cv2.filter2D(src=frame, kernel=Sharpen_Kernel, ddepth=-1)
    return Sharpen_Effect_Img
    
def sepia(frame):
    Sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    Sepia_Effect_Img = cv2.filter2D(src=frame, kernel=Sepia_Kernel, ddepth=-1)
    return Sepia_Effect_Img

def blur(frame):
    Blur_Effect_Img = cv2.GaussianBlur(frame, (35, 35), 0)
    return Blur_Effect_Img
    
def gray(frame):
    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return greyscale

def faceRecog(frame):
    ## initialize cascade default front facing facial recognition xml
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #(Self note: this should work)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
       gray,
       scaleFactor=1.5,
       minNeighbors=2, 
       ### (self note: miNeighbor increase/dec ??)###
       minSize=(30, 30),
       flags = cv2.CASCADE_SCALE_IMAGE
    )
    ## print amount of faces discovered 
    ###(self note: increase neighbors?)###
    print("Found {0} (full view) faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    
    return image

def detectShape(frame):
    # Convert input image to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Make a copy to draw bounding box
    input_image_cpy = frame.copy()
    
    threshold_value = gray_img[216, 402]
    print(threshold_value)
     
    # Convert the grayscale image to binary (image binarization opencv python)
    ret, binary_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)
     
    # Invert image
    inverted_binary_img = ~ binary_img
     
    # Detect contours
    # hierarchy variable contains information about the relationship between each contours
    contours_list, hierarchy = cv2.findContours(inverted_binary_img,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE) # Find contours
     
    # for each detected contours
    for contour_num in range(len(contours_list)):
     
        # Draw detected contour with shape name
        contour1 = cv2.drawContours(input_image_cpy, contours_list, contour_num, (255, 0, 255), 3)
     
        # Find number of points of detected contour
        end_points = cv2.approxPolyDP(contours_list[contour_num], 0.001 * cv2.arcLength(contours_list[contour_num], True), True)
     
        # Make sure contour area is large enough (Rejecting unwanted contours)
        if (cv2.contourArea(contours_list[contour_num])) > 10:
     
            # Find first point of each shape
            point_x = end_points[0][0][0]
            point_y = end_points[0][0][1]
     
            # Writing shape name at center of each shape in black color (0, 0, 0)
            text_color_black = (0, 0, 0)
     
            # If a contour have three end points, then shape should be a Triangle
            if len(end_points) == 3:
                cv2.putText(input_image_cpy, 'Triangle', (point_x, point_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color_black, 1)
     
            # If a contour have four end points, then shape should be a Rectangle or Square
            elif len(end_points) == 4:
                cv2.putText(input_image_cpy, 'Rectangle', (point_x, point_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color_black, 1)
     
            # If a contour have five end points, then shape should be a Pentagon
            elif len(end_points) == 5:
                cv2.putText(input_image_cpy, 'Pentagon', (point_x, point_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color_black, 1)
     
            # If a contour have ten end points, then shape should be a Star
            elif len(end_points) == 10:
                cv2.putText(input_image_cpy, 'Star', (point_x, point_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color_black, 1)
     
            # If a contour have more than ten end points, then shape should be a Star
            else:
                cv2.putText(input_image_cpy, 'circle', (point_x, point_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color_black, 1)
            return input_image_cpy

def giveMeEdges(frame):
    # Convert to graycsale
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    
    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image
    #print("Detecting all edges, Number of edges ==: ", edges)
    

def showing(frame, num):
    if num == 0:
        cv2.imshow("CAMMER", (frame))
    elif num == 1:
        cv2.imshow("CAMMER", emboss(frame))
    elif num == 2:
        cv2.imshow("CAMMER", sharpen(frame))
    elif num == 3:
        cv2.imshow("CAMMER", sepia(frame))
    elif num == 4:
        cv2.imshow("CAMMER", blur(frame))
    elif num == 5:
        cv2.imshow("CAMMER", gray(frame))  
    elif num == 6:
        #giveMeEdges(frame) possibly use as initial image rather than conversion
        cv2.imshow("CAMMER", detectShape(frame))  
    elif num == 7:
        cv2.imshow("CAMMER", faceRecog(frame))  

def openCam():
    cv2.namedWindow("CAMMER")
    
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    inp = 0
    while rval:
        showing(frame, inp)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            print("LATER NERD")
            break
        elif key == 49 or key == 97: # 1 and numpad 1
            inp = 0
        elif key == 50 or key == 98: # 2 and numpad 2
            inp = 1
        elif key == 51 or key == 99: # 3 and numpad 3
            inp = 2
        elif key == 52 or key == 100: # 4 and numpad 4
            inp = 3
        elif key == 53 or key == 101: # 5 and numpad 5
            inp = 4
        elif key == 54 or key == 102: # 6 and numpad 6
            inp = 5
        elif key == 55 or key == 103: # 7 and numpad 7
            inp = 6
        elif key == 56 or key == 104: # 8 and numpad 8
            inp = 7
    vc.release()
    cv2.destroyWindow("CAMMER")
    
try:
    openCam()
except KeyboardInterrupt:
    print("LATER NERD")
