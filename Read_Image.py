import cv2
import numpy as np
import matplotlib.pyplot as plt


def Read_Image_Feature(filename):
    size = (100, 100)
    thresh = 180

    img_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img_resize = cv2.resize(img_gray, size, interpolation=cv2.INTER_AREA)
    img_bw = cv2.threshold(img_resize, thresh, 255, cv2.THRESH_BINARY)[1]

    Above = img_bw[0:50, 0:101]
    Under = img_bw[50:101, 0:101]

    Above_B, Under_B = 0, 0

    for x in range(50):
        for y in range(100):
            if Above[x][y] == 0:
                Above_B += 1

    for x in range(50):
        for y in range(100):
            if Under[x][y] == 0:
                Under_B += 1

    precent_above = Above_B / 5000 * 100
    precent_under = Under_B / 5000 * 100

    x = precent_above
    y = precent_under

    return x, y

