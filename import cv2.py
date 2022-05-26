import cv2
import numpy as np

INPUT_FILE1 = 'rtsp://username:password@ip:554'
INPUT_FILE2 = 'rtsp://username:password@ip:554'
INPUT_FILE3 = 'video.mp4'
INPUT_FILE4 = 'video.avi'
 
reader1 = cv2.VideoCapture(INPUT_FILE1)
reader2 = cv2.VideoCapture(INPUT_FILE2)
reader3 = cv2.VideoCapture(INPUT_FILE3)
reader4 = cv2.VideoCapture(INPUT_FILE4)
width = int(reader1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader1.get(cv2.CAP_PROP_FRAME_HEIGHT))

 
print(reader1.isOpened())
print(reader2.isOpened())
have_more_frame = True
c = 0
while have_more_frame:
    have_more_frame, frame1 = reader1.read()
    _, frame2 = reader2.read()
    _, frame3 = reader3.read()
    _, frame4 = reader4.read()
    frame1 = cv2.resize(frame1, (width//2, height//2))
    frame2 = cv2.resize(frame2, (width//2, height//2))
    frame3 = cv2.resize(frame3, (width//2, height//2))
    frame4 = cv2.resize(frame4, (width//2, height//2))
    img1 = np.hstack((frame1, frame2))
    img2 = np.hstack((frame3, frame4))
    img = np.vstack((img1, img2))
    cv2.waitKey(1)
    frame_rz = cv2.resize(img, (1280,768))
    cv2.imshow("previewName", frame_rz)
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
            break

    c += 1
    print(str(c) + ' is ok')
 
 
reader1.release()
reader2.release()
cv2.destroyAllWindows()
