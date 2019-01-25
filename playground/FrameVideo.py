import cv2
import sys
import urllib


# extract each frame of the video
vidcap = cv2.VideoCapture('Downloaded.MOV')

success, image = vidcap.read()
count = 0
success = True

while success:
    # get frame by frame
    success, image = vidcap.read()
    
    # debug message
    print 'Read #', count, 'frame: ', success
    
    cv2.imwrite("frame%d.jpg" % count, image)
    count +=1


