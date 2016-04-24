import cv2
import numpy as np

def initImage():
    return np.ones([250,250,3])

def drawImage(canvas):
    #cv2.circle(canvas,(125,125),50,0,2,0)
    #cv2.rectangle(canvas,(100,100),(150,150),(51,0,120),2,0)
    cv2.putText(canvas,"Fantastical", (80,125), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0))
    return canvas

def displayImage(canvas):
    cv2.imshow('Canvas',canvas)
    cv2.waitKey(-1)


im = drawImage(initImage())
displayImage(im)
cv2.destroyAllWindows()
