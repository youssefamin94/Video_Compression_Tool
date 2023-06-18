import sys, ffmpeg

#path of the the FFMPEG library
sys.path.append(r"C:\ffmpeg\bin")

#importing the targted video
video = ffmpeg.input('input.mp4')

#setting the desired frames per second rate
#typically the standard for the frames per second rate is 23.98 frames per second,
#decreasing fps decreases the number of frames that need to be decompressed,
#hence, decreasing the fps by a quarter of its value makes the decompressed video smaller in size and does not compramises the smooth flow of the video.

video = video.filter('fps',fps=24*0.75,round='up')

#Getting desired width 
width = int(input("Enter the width you the video to be compressed to: "))

#Getting desired height 
height = int(input("Enter the height you the video to be compressed to: "))

#Scaling the video to desired dimensions 
video = video.filter('scale', w=width,h=height)

#Saving the video
result = ffmpeg.output(video,'resultbyffmpeg.mp4')

ffmpeg.run(result)

print('Video has been compressed!')