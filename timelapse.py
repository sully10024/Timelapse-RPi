import pygame, pygame.camera, pygame.image
from pygame.locals import *
from datetime import datetime
from time import sleep, time

pygame.init()
pygame.camera.init()
webcam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (1280, 720))
webcam.start()
sleep(1)  # this allows the first picture to be taken properly

# HOW OFTEN DO YOU WANT TO TAKE A PICTURE?
HOUR_INTERVAL = 0
MINUTE_INTERVAL = 2
# HOW LONG TO WAIT BEFORE TIMELAPSE STARTS?
HOURS = 0
MINUTES = 0
SECONDS = 0

# print when the first photo will be taken
print "The first photo will be taken in:"
print str(HOURS) + " hours"
print str(MINUTES) + " minutes"
print str(SECONDS) + " seconds"

# set the settings
DELAY_TIME = (HOUR_INTERVAL*3600 + MINUTE_INTERVAL*60)
sleep(HOURS*3600 + MINUTES*60 + SECONDS)

# the actual timelapse stuff
while True:
    startTime = time()

    for x in range (0,5):  # this warms up the camera by taking 5 pictures without saving them
        webcam.get_image()
    
    name = datetime.now().strftime('%Y-%d-%m--%H-%M') + ".jpeg"    # year-day-month--24hour-minute.jpeg
    
    pygame.image.save(webcam.get_image(), "photos/" + name)   # saves the photo to the photos directory
    sleep(1)    # just in case (this might not be necessary though)

    totalTime = time() - startTime    # how long this cycle took to take

    print "Took " + name + " in " + str(totalTime) + " seconds"

    sleep(DELAY_TIME- totalTime)  # accounts for the time it took to warm up and take the photo
