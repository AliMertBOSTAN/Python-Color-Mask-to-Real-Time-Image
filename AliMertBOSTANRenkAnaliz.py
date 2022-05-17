import cv2
import numpy as np
import pandas as pd

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    cv2.imshow('lab', lab)
    cv2.imshow('hsv', hsv)
    cv2.imshow('hls', hls)

    lower_hsv = np.array([0, 0, 0])
    upper_hsv = np.array([100, 100, 100])

    lower_bgr = np.array([0, 0, 0])
    upper_bgr = np.array([100, 100, 100])

    lower_lab = np.array([0, 0, 0])
    upper_lab = np.array([100, 100, 100])

    lower_hls = np.array([0, 0, 0])
    upper_hls = np.array([100, 100, 100])    

    maskhsv = cv2.inRange(hsv, lower_hsv, upper_hsv)
    maskbgr = cv2.inRange(frame, lower_bgr, upper_bgr)
    masklab = cv2.inRange(lab, lower_lab, upper_lab)
    maskhls = cv2.inRange(hls, lower_hls, upper_hls)
    

    

    cv2.imshow('masklab', masklab)
    cv2.imshow('maskbgr', maskbgr)
    cv2.imshow('maskhsv', maskhsv)
    cv2.imshow('Normal', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('maskshls', hls)
    cv2.imshow('maskshls', maskhls)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
