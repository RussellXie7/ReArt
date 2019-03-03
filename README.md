# Re:Art
This is the repository for our SDHacks project Re:Art, including the website design, the back-end server backup, and the algorithm used for automating image processing and style transfer using Convolutional Neural Network

* **Devpost**: https://devpost.com/software/re-art-f92i1b
* **Media Exposure**: https://cse.ucsd.edu/about/news/cse-sophomores-take-top-prize-sd-hacks-2016

## Introduction
Re: Art is an awards-winning web app that implemented convolutional neural network to allow transforming an uploaded video into animated artwork as if it was drawn by artist like Van Gogh. We built this app at SD Hacks 2016, making it the first video style transfer web app on the internet, and showered with prizes including Best of Show, Best Use of AWS, and Most Commercializable Hack. Check out our project on the Devpost to see how it works!

### Examples:
#### Source of Style:
![alt text](https://github.com/RussellXie7/ReArt/blob/master/Desktop/vango.jpg?raw=true)

#### Output of user-uploaded video:
![alt text](https://github.com/RussellXie7/ReArt/blob/master/Desktop/output2.gif?raw=true)

## Inspiration and Background
At the time when we were developing this webapp, Prisma just had its debut and won a lot of popularity with its style transfer filter for images, but its functionalities are only limited to processing images instead of videos at that time (09/2016). We, therefore, wanted to make the video artistic as well, so we created this project Re:Art. Interestingly, 2 weeks after our application was published in the Hackathon, Prisma released the video style transfer feature for their application as well.

## Built With

* [Node.js](https://nodejs.org/en/)
* [PyTorch](https://pytorch.org/)
* [Python 2.7](https://www.python.org/)
* [OpenCV](https://opencv.org/)


## How does it work:

### Back-end

We set up a comprehensive back-end still image stylization service based on the AWS and G2 instance in the EC2 service. We achieve the non-linear video processing result through Open CV (Open Source Computer Vision), which enable the web app Re:Art allowing users to process a self-designed animated artwork.

### User Flow:

* **Read user input:** When a user uploads a video and chooses a picture style, we will read in the video and style they choose, and we will decide the frame number based on how long we want the output gif file to be.

* **Transform the video:** We pick up the images based on the frame rate, and then crop the images into the size with the ratio 8.5:11, which is roughly 300px * 388px. Also, we uses advanced compression algorithm to make the image further smaller without losing much of its original quality. Due to the undesirable efficiency of the Neural Network Framework, we came up with several ways to increase our efficiency use multi-parallel subprocess to transform the image simultaneously, and use the resources of the server to its maximum. Because we depend on GPU rather than CPU to have a better performance, we chose the AWS instance that has more GPUs. Because the feature of the Open Source Torch Framework is based on Lua, we manipulate the iteration time on each image to achieve an effect of transition, giving user a feeling of more dynamic stylized images.

* **Output Gif:** We store the image to an array and restructure them to form a gif, which is finally presented to the user.

### Front-end

We designed a user-friendly Web App using HTML5, CSS, JavaScript, JQuery to orient the users to upload their videos, choose a style that they prefer and follow the page to finally get the stylized gif. On our home page, we designed as few icons and concise instructions as possible to make it clear to the new users on how to use the app. After uploading a video, the user can choose within a scroll bar several different styles of artworks to merge the video with. Then our app throws the job to the server to complete stylization process. When it’s done, the user is directed to another page where he/she can view the resulting gif and share it to Facebook, Twitter, Google Plus etc.

## Developers Team

* **Wanze (Russell) Xie** - (https://github.com/russellxie7)
* **Jianhan Xu** - (https://github.com/Jorx11)
* **Chen Yang** - (https://github.com/azureric)
* **Zhuojun Chen**

## Awards
* **Best of Show** by SDHacks Committee
* **Best Use of AWS** by Amazon.com Inc.
* **Most Commercializable Hack** presented by the UCSD Office of Innovation and Commercialization

