from ctypes import Union
from typing import Dict, Tuple
import cv2
from os import path
import numpy as np
from matplotlib import pyplot as plt
from config import config

# res = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)
def colorMatch(img_hsv, lower, upper):
    return cv2.inRange(img_hsv, lower, upper)

# morphological process
def morphoProcess(img, shape = cv2.MORPH_RECT, kenel_size = (20, 20)):
    kenel = cv2.getStructuringElement(shape, kenel_size)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kenel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kenel)
    return closing

# find the target contours (the topmost contours here)
def matchTarget(img):
    target: Dict[str, Union[np.ndarray, Tuple[int]]] = {}

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_with_topmost = sorted([(cnt, tuple(cnt[cnt[:, :, 1].argmin()][0])) for cnt in contours], key = lambda x: x[1][1])
    for cnt in cnt_with_topmost:
        M = cv2.moments(cnt[0])
        area = M["m00"]
        if area > config.MIN_AREA:
            target["centroid"] = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
            target["cnt"] = cnt[0]
            break
    if len(target) == 0:
        M = cv2.moments(cnt_with_topmost[0][0])
        target["cnt"] = cnt_with_topmost[0][0]
        target["centroid"] = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
    return target

if __name__ == "__main__":
    img_bgr = cv2.imread(f"{path.dirname(__file__)}/assets/demo_1.jpg")

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    matched_mask = colorMatch(img_hsv, np.array([10, 60, 240]), np.array([25, 100, 255]))
    result = morphoProcess(matched_mask)

    plt.subplot(121), plt.imshow(result, cmap = "gray"), plt.title("mask")

    target = matchTarget(result)
    cv2.drawContours(img_bgr, [target["cnt"]], 0, (0, 0, 255), 10)
    cv2.drawMarker(img_bgr, tuple(target["centroid"]), (0 ,0, 255), thickness = 10, markerSize = 50)

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.subplot(122), plt.imshow(img_rgb), plt.title("target")
    plt.show()
    