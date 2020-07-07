import cv2
import numpy


class Test:
    def main(self):
        filepaths_cascade = (
            'haarcascade_frontalface_default.xml',
            'haarcascade_frontalface_alt.xml',
            'haarcascade_frontalface_alt2.xml',
            'haarcascade_frontalface_alt_tree.xml')
        filepath_cascade = filepaths_cascade[0]

        # Prepare capture
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception('Capture cannot opened')
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        # Create CVWindow
        cv2.namedWindow('test', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('test', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Create image for print
        image_show = numpy.zeros((480, 800, 3), numpy.uint8)

        # Prepare cascade
        cascade = cv2.CascadeClassifier(filepath_cascade)

        while True:
            # Read frame
            ret, image = cap.read()

            # Analyse frame
            image_grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            rects = cascade.detectMultiScale(image_grayscaled)

            # Show result
            for rect in rects:
                cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=1)
            image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_NEAREST)
            image_show[:, 80:720, :] = image[:, ::-1, :]
            cv2.imshow('test', image_show)

            # Check whether the program should exit or coutinue
            if cv2.waitKey(1) != 255:
                break

        # Finalise
        cap.release()
        cv2.destroyAllWindows()
