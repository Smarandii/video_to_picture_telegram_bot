import cv2
import os


def get_firstrame(filename):
    cap = cv2.VideoCapture(filename)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')
    ret, frame = cap.read()
    name = './data/frame.jpg'
    cv2.imwrite(name, frame)
    cap.release()
    cv2.destroyAllWindows()
    return True
