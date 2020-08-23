import cv2 as cv
import numpy as np

full_image = cv.imread('test_full_screenshot.png', cv.IMREAD_UNCHANGED)
green_image = cv.imread('test_green_part.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(full_image, green_image, cv.TM_CCOEFF_NORMED)

# gives best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('best match top left position : %s' % str(max_loc))
print('best match top confidence : %s' % max_val)

threshold = 0.8

if max_val >= threshold:
    print("found green")

    green_image_w = green_image.shape[1]
    green_image_h = green_image.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + green_image_w, top_left[1] + green_image_h)

    cv.rectangle(full_image,top_left, bottom_right, color=(255, 0, 0), thickness=2,lineType=cv.LINE_4)

    cv.imshow("result", full_image)
    cv.waitKey()
else:
    print('no green found')
# cv.imshow('Result', result)
# cv.waitKey()
