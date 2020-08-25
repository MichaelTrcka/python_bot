import cv2 as cv
import os
from time import time
from util.window_capture import WindowCapture
from util.vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('RuneLite - TRCKAMAN')

vision_tree = Vision('resources/cow.jpg')

loop_time = time()
while True:
    screenshot = wincap.get_screenshot()

    points = vision_tree.find(screenshot, 0.8, 'rectangles')

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('done')
