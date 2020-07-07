import time
import statistics
import cv2


class Test:
    FILEPATH_IMAGE = 'test1.jpg'

    image_cv = None

    @staticmethod
    def initialize():
        cv2.namedWindow(Test.FILEPATH_IMAGE)

    @staticmethod
    def read_image(filepath):
        Test.image_cv = cv2.imread(filepath)

    @staticmethod
    def draw_image():
        cv2.imshow(Test.FILEPATH_IMAGE, Test.image_cv)

    @staticmethod
    def finalize():
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

    @staticmethod
    def main():
        Test.initialize()
        Test.read_image(Test.FILEPATH_IMAGE)

        time_results = []
        for i in range(100):
            time_start = time.perf_counter()
            Test.read_image(Test.FILEPATH_IMAGE)
            Test.draw_image()
            time_end = time.perf_counter()
            time_results.append(time_end - time_start)
        print('read_image + draw_image: {0:.1f}fps'.format(1.0 / statistics.mean(time_results)))
        for time_result in time_results:
            print('    {0:.1f}fps'.format(1.0 / time_result))

        Test.finalize()
