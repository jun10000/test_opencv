import time
import cv2


class Test:
    image = None
    image_grayscaled = None
    cascade = None

    def open_window(self, title):
        cv2.namedWindow(title)

    def read_image(self, filepath):
        self.image = cv2.imread(filepath)
        self.image_grayscaled = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def read_cascade(self, filepath):
        self.cascade = cv2.CascadeClassifier(filepath)

    def draw_result(self, window_title):
        rects = self.cascade.detectMultiScale(self.image_grayscaled)
        for rect in rects:
            cv2.rectangle(self.image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
        cv2.imshow(window_title, self.image)

    def wait(self):
        cv2.waitKey(3000)

    def close_windows(self):
        cv2.destroyAllWindows()

    def main(self):
        filepaths_image = (
            'test1.jpg',
            'test2.jpg')
        filepaths_cascade = (
            'haarcascade_frontalface_default.xml',
            'haarcascade_frontalface_alt.xml',
            'haarcascade_frontalface_alt2.xml',
            'haarcascade_frontalface_alt_tree.xml')

        self.open_window(filepaths_image[1])
        self.read_cascade(filepaths_cascade[0])

        time_start = time.perf_counter()
        self.read_image(filepaths_image[1])
        self.draw_result(filepaths_image[1])
        time_end = time.perf_counter()
        print('result: {0:.1f}fps'.format(1.0 / (time_end - time_start)))

        self.wait()
        self.close_windows()
