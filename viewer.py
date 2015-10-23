#A simple program to display one image, then play a movie

import os
import signal
import time
import subprocess 

movie_path = 'Game Jam Fal 2014 Trailer_1-Broadband High.mp4'
image_path = 'labhours2.jpg'

time.sleep(5)

while True:
	image = subprocess.Popen(['fim',image_path,'-a'])
	time.sleep(45)
	omxp = subprocess.Popen(['omxplayer',movie_path, '-b'])
	time.sleep(76)
	image.kill()
	omxp.kill()
