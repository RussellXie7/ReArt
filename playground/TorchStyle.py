import sys
import subprocess
import imageio
import urllib

# fps of the gif
number_list = sys.argv[1]
style_image = sys.argv[2]

# the array of images awating for stylization
images = []

for index in number_list:
    images.append(imageio.imread('Scaled%d.jpg' % index))
    # debug
    print "Adding the image Scaled #",index


# Call the Torch script, with increasing iteration
iteration = 1000 / len(number_list)
currIteration = 0
loopCount = 0

# increasing the iteration times in each loop
for singleImage in images:
    currIteration += iteration

    subprocess.call([sys.executable], 'neural_style.py', '--content',
        singleImage,'--styles',style_image, '--iterations', currIteration, 
        '--out', 'Processed%d.jpg' % loopCount)
    
    # delete the cropped images, since they have been tranformed
    subprocess.call(["rm", "Scaled%d.jpg" % number_list[loopCount]])

    loopCount += 1


# processed images will be stored in sequence, as Processed0.jpg ... 




