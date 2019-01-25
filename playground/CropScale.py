import cv2
from PIL import Image
import subprocess
import sys

image_number = int(sys.argv[1])

img = cv2.imread("frame%d.jpg" % image_number)
imgHeight, imgWidth, imgChannel = img.shape

print imgHeight, imgWidth

if imgHeight > imgWidth:
	newHeight = imgWidth * (11 / 8.5)
else:
	newHeight = imgHeight

startHeight = int((imgHeight - newHeight) / 2)

endHeight = int(startHeight + newHeight)

crop_img = img[startHeight:endHeight, 0:imgWidth]
cv2.imwrite("Cropped%d.jpg" % image_number,crop_img)

foo = Image.open("Cropped%d.jpg" % image_number)
foocv = cv2.imread("Cropped%d.jpg" % image_number)
height,width,channel = foocv.shape

# debug
print height, width

height = int(height * 0.3)
width = int(width * 0.3)

foo = foo.resize((width,height),Image.ANTIALIAS)


foo.save("Scaled1.jpg", optimize=True,  quality = 85)

subprocess.call(["rm","Cropped%d.jpg" % image_number])
