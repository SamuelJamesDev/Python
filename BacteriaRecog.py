#this program breaks up and counts bacteria in a given image:
## Final Method ###
## Imports
import matplotlib.pyplot as plt
import imutils
import cv2
import numpy as numpy

## load image in cv
img = cv2.imread('bacteria.jpg')

## set grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## create negative image for processing
gray = 255-gray

## display unlabeled image
plt.imshow(gray, cmap='gray',
           vmin=0,vmax=255)
plt.show()

## define threshold
## after removing excess noise by altering the image to a negative image
## call cv2.canny as edge detection to better recognize shapes in the image
## while also removing the outermost 
## contour and other noise being counted as a contour
canny = cv2.Canny(gray, 100, 200, 3, L2gradient=True)

## using canny as the threshold and setting the rgb max values we define our
## threshold to be used within our image
ret,thresh = cv2.threshold(canny,127,255,2)

## find contours working, drawContours issue again
(_, cnts, h) = cv2.findContours(thresh,
                                cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
## utilizing RETR_TREE we can find each individual contour within the heirarchy 

## for loop to draw each contour
for c in cnts: 
    cv2.drawContours(img, [c], -1, (255, 0, 0), 1)   

## len(cnts) will return the count of objects by counting each objects contour
## display new image
print(len(cnts), "bacteria found within image")
plt.imshow(img)

## write and save the resulting image
cv2.imwrite('results.png', img)
plt.show()
