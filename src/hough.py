import cv2
import numpy as np

from read import read_in_image

def hough(fp):
    """ Detect lines with CV2's Hough Line Transform

    Ref:
        - https://docs.opencv.org/3.4/d3/de6/tutorial_js_houghlines.html
        - https://learnopencv.com/hough-transform-with-opencv-c-python
    """
    # TODO remove magic number
    threshold: int = 2
    # read in
    _img = read_in_image(fp)
    img = cv2.imread(_img, cv2.IMREAD_COLOR) # road.png is the filename
    # image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # find edges using canny detector
    edges = cv2.Canny(gray, 50, 200)
    # detect the points that form a line
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold, minLineLength=10, maxLineGap=250)
    # draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    return img