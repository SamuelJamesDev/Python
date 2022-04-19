from PIL import Image
import cv2 
import sys
import matplotlib.pyplot as plt
# this is facial reccognition not requiring cv2 for every process #

## cv2 start window required to prevent colab exception
cv2.startWindowThread()
#*********************facialRecognitionFunction******************************#
def FacialRecognition(filename):
  # create image path and open image for display
  imagePath = filename
  img = Image.open(filename)
  # display the original image for comparison
  plt.imshow(img)
  plt.show()
  ## initialize cascade default front facing facial recognition xml
  cascPath = "/content/haarcascade_frontalface_default.xml"

  # Create the haar cascade
  faceCascade = cv2.CascadeClassifier(cascPath)

  # Read the image
  image = cv2.imread(imagePath)
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

  ## colab cannot utilize cv2.imshow() use plt.imshow of the cvtColor
  plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.show()
#***************************************************************************#


# Using the facial recognition function on jpg file
#***************************************************************************#
# initialize method using input from user
g = input('Enter jpg File Name: ') 
g = g + '.jpg'
FacialRecognition(g)
#***************************************************************************#
