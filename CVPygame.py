import time
import statistics
import cv2
import pygame


class Test:
    FILEPATH_IMAGE = 'test1.jpg'

    image_surface = None
    screen = None

    @staticmethod
    def initialize():
        pygame.init()

    @staticmethod
    def read_image(filepath):
        image_cv = cv2.imread(filepath)
        mode_convert = cv2.COLOR_GRAY2RGB if (len(image_cv.shape) == 2) else cv2.COLOR_BGR2RGB
        image_cv_converted = cv2.cvtColor(image_cv, mode_convert).swapaxes(0, 1)
        if Test.image_surface is None:
            Test.image_surface = pygame.surfarray.make_surface(image_cv_converted)
            image_size = Test.image_surface.get_size()
            Test.screen = pygame.display.set_mode(image_size)
        else:
            pygame.surfarray.blit_array(Test.image_surface, image_cv_converted)

    @staticmethod
    def draw_image():
        Test.screen.blit(Test.image_surface, (0, 0))
        pygame.display.update()

    @staticmethod
    def finalize():
        pygame.quit()

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
        time_results.pop(0)
        print('read_image + draw_image: {0:.1f}fps'.format(1.0 / statistics.mean(time_results)))
        for time_result in time_results:
            print('    {0:.1f}fps'.format(1.0 / time_result))

        Test.finalize()
