import cv2
from os import path
from matplotlib import pyplot as plt

def matchTiger(img, tiger):
    tiger_gray = cv2.cvtColor(tiger, cv2.COLOR_BGR2GRAY)
    h, w = tiger_gray.shape
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, tiger_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return (top_left, w, h)

if __name__ == "__main__":
    tiger_bgr = cv2.imread(f"{path.dirname(__file__)}/assets/tiger-left.jpg")
    img_bgr = cv2.imread(f"{path.dirname(__file__)}/assets/demo_1.jpg")
    top_left, w, h = matchTiger(img_bgr, tiger_bgr)

    cv2.rectangle(img_bgr, top_left, (top_left[0] + w, top_left[1] + h), 0, 5)
    plt.imshow(img_bgr[:, :, ::-1]), plt.title("result")
    plt.show()
