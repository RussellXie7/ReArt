import imageio
import sys

# the array of images
images = []
# total number of processed images
number_of_images = int(sys.argv[1])


for count in range(0, number_of_images):
	images.append(imageio.imread('Processed%d.jpg' % count))
	# debug
	print "In GifMaster: ", count

imageio.mimsave('output.gif',images)

# delelted the processed images
for number in range(0, number_of_images):
	subprocess.call(["rm", "Processed%d.jpg" % number])

