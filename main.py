import time
import random
import cv2
import keyboard
import numpy as np

from PIL import ImageGrab

cast = True
fishing = cv2.imread('image.png', 0)
templateWidth, templateHeight = fishing.shape[::-1]

print("Fishing will be started in 5 seconds!")
time.sleep(5)
print("Started!")

while True:
    if (cast):
        print("Casting out lure")
        keyboard.press_and_release('e')
        cast = False
        continue

    imagePixels = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    pixelsNumpy = np.array(imagePixels)

    grayscaleImage = cv2.cvtColor(pixelsNumpy, cv2.COLOR_BGR2GRAY)
    templateMatch = cv2.matchTemplate(
        grayscaleImage, fishing, cv2.TM_CCOEFF_NORMED)
    matchLocations = np.where(templateMatch >= 0.8)

    for point in zip(*matchLocations[::-1]):
        if point != None:
            print("Detected catch! Reeling in lure")
            keyboard.press_and_release('e')
            cast = True
            time.sleep(random.uniform(6, 7.5))
            break

    time.sleep(0.100)
