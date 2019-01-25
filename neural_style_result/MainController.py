import cv2
import sys
import urllib
import subprocess
import imageio
import Image
from moviepy.editor import VideoFileClip

def frame_video():
    
    # extract each frame of the video
    vidcap = cv2.VideoCapture('Downloaded.MOV')

    success, image = vidcap.read()
    count = 0
    success = True

    while success:
        # get frame by frame
        success, image = vidcap.read()
        
        if not success:
            break

        # debug message
        print 'Read #', count, 'frame: ', success

        cv2.imwrite("frame%d.jpg" % count, image)

        img = Image.open("frame%d.jpg" % count)

        img = img.rotate(-90)
        img.save("frame%d.jpg" % count)

        count +=1

    return count



def cropScale(image_number):

    img = cv2.imread("frame%d.jpg" % image_number)
    imgHeight, imgWidth, imgChannel = img.shape

    print imgHeight, imgWidth

    if imgHeight > imgWidth:
        newHeight = imgWidth * (11 / 8.5)
    
        startHeight = int((imgHeight - newHeight) / 2)
    
        endHeight = int(startHeight + newHeight)

        crop_img = img[startHeight:endHeight, 0:imgWidth]


    else:
        newWidth = imgHeight * (11 / 8.5)

        startWidth = int((imgWidth - newWidth) / 2)

        endWidth = int(startWidth + newWidth)

        crop_img = img[0:imgHeight, startWidth:endWidth]

    
    cv2.imwrite("Cropped%d.jpg" % image_number,crop_img)


    # Scale the image
    foo = Image.open("Cropped%d.jpg" % image_number)
    foocv = cv2.imread("Cropped%d.jpg" % image_number)
    height,width,channel = foocv.shape

    # debug
    print height, width

    height = int(height * 0.3)
    width = int(width * 0.3)

    foo = foo.resize((width,height),Image.ANTIALIAS)

    foo.save("Scaled%d.jpg" % image_number, optimize=True,  quality = 85)
    
    print "Saved..."

    subprocess.call(["rm","Cropped%d.jpg" % image_number])



def torchStyle(number_list, style_image):

    # the array of images awating for stylization
    #images = []

    #for index in number_list:
        # debug
        #print "Adding the image Scaled #",index
        #images.append(imageio.imread('Scaled%d.jpg' % index))

    # Call the Torch script, with increasing iteration
    print "The length of number_list is ", len(number_list)
    
    maxIteration = 600
    minIteration = 500

    iteration = (maxIteration - minIteration) / len(number_list)
    currIteration = maxIteration
    
    loopCount = 0

    # increasing the iteration times in each loop
    #for singleImage in images:
    for index in range(0, len(number_list), 4):
        
        currIteration -= iteration
        
        if currIteration < minIteration:
            break

        print "The current Iteration time is ", currIteration
        print "The loopCount is ", loopCount

        gpuValue = 0

        # Coroutine
        p1 = subprocess.Popen(['th', '../neural-style/neural_style.lua', '-style_image', style_image, 
            '-content_image', 'Scaled%d.jpg' % number_list[loopCount], '-output_image', 'Processed%d.jpg' % loopCount,
            '-backend', 'cudnn', '-cudnn_autotune', '-optimizer', 'adam', '-image_size', '256', '-gpu','%d' % gpuValue,
            '-num_iterations', '%d' % currIteration]) 


        loopCount += 1
        gpuValue += 1


        currIteration -= iteration

        if currIteration < minIteration:
            p1.wait()
            break

        print "The current Iteration time is ", currIteration
        print "The loopCount is ", loopCount

        p2 = subprocess.Popen(['th', '../neural-style/neural_style.lua', '-style_image', style_image, 
            '-content_image', 'Scaled%d.jpg' % number_list[loopCount], '-output_image', 'Processed%d.jpg' % loopCount,
            '-backend', 'cudnn', '-cudnn_autotune', '-optimizer', 'adam', '-image_size', '256', '-gpu','%d' % gpuValue,
            '-num_iterations', '%d' % currIteration]) 

        loopCount += 1
        gpuValue += 1


        currIteration -= iteration

        if currIteration < minIteration:
            p1.wait()
            p2.wait()
            break

        print "The current Iteration time is ", currIteration
        print "The loopCount is ", loopCount
        
        p3 = subprocess.Popen(['th', '../neural-style/neural_style.lua', '-style_image', style_image, 
            '-content_image', 'Scaled%d.jpg' % number_list[loopCount], '-output_image', 'Processed%d.jpg' % loopCount,
            '-backend', 'cudnn', '-cudnn_autotune', '-optimizer', 'adam', '-image_size', '256','-gpu','%d' % gpuValue, 
            '-num_iterations', '%d' % currIteration]) 

        loopCount += 1
        gpuValue += 1


        currIteration -= iteration

        if currIteration < minIteration:
            p1.wait()
            p2.wait()
            p3.wait()
            break

        print "The current Iteration time is ", currIteration
        print "The loopCount is ", loopCount
        
        p4 = subprocess.Popen(['th', '../neural-style/neural_style.lua', '-style_image', style_image, 
            '-content_image', 'Scaled%d.jpg' % number_list[loopCount], '-output_image', 'Processed%d.jpg' % loopCount,
            '-backend', 'cudnn', '-cudnn_autotune', '-optimizer', 'adam', '-image_size', '256', '-gpu','%d' % gpuValue,
            '-num_iterations', '%d' % currIteration]) 


        loopCount += 1

        # wait until every one finished
        exit_codes = [p.wait() for p in p1, p2, p3, p4]



    for index in range (0, len(number_list)):
        # delete the cropped images, since they have been tranformed
        subprocess.call(["rm", "Scaled%d.jpg" % number_list[index]])

    # processed images will be stored in sequence, as Processed0.jpg ... 



def gifMaster(number_of_images):

    # the array of images
    images = []

    for count in range(0, number_of_images):
        images.append(imageio.imread('Processed%d.jpg' % count))
        # debug
        print "In gifMaster: ", count

    imageio.mimsave('output.gif',images)

    # delelted the processed images
    for number in range(0, number_of_images):
        print "Removed Once"
        subprocess.call(["rm", "Processed%d.jpg" % number])

     
def main():
    # the URL of the video
    URL = sys.argv[1]
    # the fps of the gif
    fps = int(sys.argv[2])
    # the image style we want, based on current directory
    style_image = sys.argv[3]

    # download the URL file and save to cwd
    f = open('Downloaded.MOV','wb')
    f.write(urllib.urlopen(URL).read())
    f.close()

    # extract each frame and save as jpg
    count = frame_video()

    # get the length of this video
    clip = VideoFileClip("Downloaded.MOV")
    duration = clip.duration

    #debug
    print "Time taken: {0} seconds".format(duration)
    original_fps = count / duration
    print "Estimated frames per second: {0}".format(original_fps)
    
    # We assume fps is smaller than original_fps
    jump_number = int(original_fps / fps)

    
    # possible bug
    # the number order of the frames remained
    numberList = []

    x = 0
    for index in range(0, int(count / jump_number)):
        numberList.append(x)
        cropScale(x)
        x += jump_number

    # delete all the frame jpg
    for index in range(0, count):
        subprocess.call(["rm","frame%d.jpg" % index])

    print "The size of the list is : ",len(numberList)

    print "Call Torch"
    # now all the necessary photos have been cropped and scaled
    torchStyle(numberList, style_image)

    # call the gif generator
    gifMaster(len(numberList))



if __name__ == '__main__':
    
    main()

    #numberListtest = [0]
    #style_image = sys.argv[1]
    #torchStyle(numberListtest,style_image)


