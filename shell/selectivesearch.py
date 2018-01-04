import cv2
import selectivesearch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

def easydetection(filename):
    print(filename)
    img = cv2.imread("./image/"+filename)
    img_lbl, regions = selectivesearch.selective_search(img, scale=500, sigma=0.9, min_size=10)
    candidates = set()
    max = set()
    temp_max = 0
    temp_sec = 0
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 2000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.2:
            continue
        if(temp_max==w*h):
            continue
        elif(temp_max<w*h):
            candidates = max
            max = set()
            max.add(r['rect'])
            temp_sec = temp_max
            temp_max = w*h
        else:
            if(temp_sec == w*h):
                continue
            elif(temp_sec<w*h):
                candidates.clear()
                candidates.add(r['rect'])
                temp_sec = w*h
            else:
                continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)
    plt.savefig("./deal/"+filename)

if __name__ == "__main__":
    img_name = os.listdir("/Users/chenhai/PycharmProjects/DetectionLocation/image/")
    for name in img_name:
        if "JPEG" in name:
            easydetection(name)
        else:
            continue



