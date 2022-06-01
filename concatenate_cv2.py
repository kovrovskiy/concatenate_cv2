import cv2
import sys
import numpy as np
from win32api import GetSystemMetrics

INPUT_FILE1 = 'rtsp://username:password@ip:554'
INPUT_FILE2 = 'rtsp://username:password@ip:554'
INPUT_FILE3 = 'video.mp4'
INPUT_FILE4 = 'video.avi'
 
stream1 = cv2.VideoCapture(INPUT_FILE1)
stream2 = cv2.VideoCapture(INPUT_FILE2)
stream3 = cv2.VideoCapture(INPUT_FILE3)
stream4 = cv2.VideoCapture(INPUT_FILE4)
width = int(stream1.get(3))
height = int(stream1.get(4))



while (stream1.isOpened()):
    ret, frame1 = stream1.read()
    _, frame2 = stream2.read()
    _, frame3 = stream3.read()
    _, frame4 = stream4.read()
    frame_rz1 = cv2.resize(frame1, (width//2, height//2))
    frame_rz2 = cv2.resize(frame2, (width//2, height//2))
    frame_rz3 = cv2.resize(frame3, (width//2, height//2))
    frame_rz4 = cv2.resize(frame4, (width//2, height//2))
    width_mon = GetSystemMetrics(0)
    height_mon = GetSystemMetrics(1)
    img1 = np.hstack((frame_rz1, frame_rz2))
    img2 = np.hstack((frame_rz3, frame_rz4))
    img = np.vstack((img1, img2))
    frame_rs = cv2.resize(img, (width_mon,height_mon))
    cv2.imshow(f'IP Camera', frame_rs)
    if cv2.waitKey(1) == 27: #27 - Esc
        sys.exit() 
stream1.release()
stream2.release()
stream3.release()
stream4.release()
cv2.destroyAllWindows()