from random import randint
import cv2
from matcher.colorMatcher import morphoProcess, matchTarget, colorMatch
from matcher.tmpMatcher import matchTiger
from os import path
import numpy as np
from controller.adbController import screenCap, press
from keyboard import wait, hook_key
from config import config
from debug.debug import enableRecorder

def calDistance(start, end):
    return int(((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5)

def jump(distance):
    size = config.SIZE
    duration = int(config.COEFFICIENT * distance)
    y_min, y_max, x_min, x_max = size[1] * 2 // 3, size[1], size[0] // 3, size[0] * 2 // 3
    random_pos = (randint(x_min, x_max), randint(y_min, y_max))
    press(random_pos, duration)




def main():
    # enable debug
    updateRecorder = enableRecorder()
    shouldContinue = True
    def callback():
        nonlocal shouldContinue 
        shouldContinue = False
    hook_key("esc", callback)
    tiger_bgr = cv2.imread(f"{path.dirname(__file__)}/assets/tiger-left.jpg")
    while shouldContinue:
        print("wait for capture screen and calculate distance ...")
        wait("enter")
        screenCap()
        img_bgr = cv2.imread(f"{path.dirname(__file__)}/assets/demo.png")
        # find tiger
        top_left, w, h = matchTiger(img_bgr, tiger_bgr)
        start_point = (top_left[0] + int(w / 2), top_left[1] + h)
        # find destination
        img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
        matched_mask = colorMatch(img_hsv, config.MIN_HSV, config.MAX_HSV)
        result = morphoProcess(matched_mask)
        target = matchTarget(result)
        end_point = target["centroid"]
        # calculate
        distance = calDistance(start_point, end_point)
        # update debug recorder
        updateRecorder(img_bgr, top_left, w, h, target)
        print(f"""
            系数: {config.COEFFICIENT}  距离:{distance}
            按压时间: {int(config.COEFFICIENT * distance)}
        """)
        print("Calculation completed, ready to jump")
        wait("enter")
        jump(distance)
        

if __name__ == "__main__":
    main()

