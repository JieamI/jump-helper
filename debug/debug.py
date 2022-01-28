import cv2
from matplotlib import pyplot as plt
from multiprocessing import Process, Queue

que = Queue()

def recorder(que = que):
    fig = plt.figure(num = "Recorder")
    ax = fig.add_subplot(111)
    plt.ion()
    while True:
        if que.empty():
            fig.canvas.flush_events()
            continue
        img_bgr, top_left, w, h, target = que.get()
        cv2.rectangle(img_bgr, top_left, (top_left[0] + w, top_left[1] + h), 0, 5)
        cv2.drawContours(img_bgr, [target["cnt"]], 0, (0, 0, 255), 10)
        cv2.drawMarker(img_bgr, tuple(target["centroid"]), (0 ,0, 255), thickness = 10, markerSize = 50)
        cv2.drawMarker(img_bgr, (top_left[0] + int(w / 2), top_left[1] + h), (0, 0, 255), thickness = 10, markerSize = 50)
        ax.imshow(img_bgr[:, :, ::-1])
        plt.show()

def enableRecorder(que = que):
    p = Process(target = recorder, daemon = True, args = (que, ))
    p.start()
    def updateRecorder(img_bgr, top_left, w, h, target):
        data = [img_bgr, top_left, w, h, target]
        que.put(data)
    return updateRecorder
    
