import logging
from time import sleep
import threading


class MyCounter:
    """
    Just an object for testing purpose
    """
    def __init__(self, name: str, pause=1) -> None:
        """
        Set name of the object and pause period for loops within it
        :param name: str
        :param pause: int
        """
        self.name = name
        self.pause = pause

    def count(self, n: int) -> None:
        """
        Print numbers from 1 to n with pausing in 1 sec
        :param n: int for counting
        :return: None
        """
        logging.info(
            f'{self.name} will count to {n} with {self.pause} sec pause')
        for i in range(n):
            logging.info(f'{self.name} says {i + 1}')
            sleep(self.pause)
        logging.info(f'{self.name} has been finished')


c1 = MyCounter('Counter-1', 2)  # set pause to 2 for clarity differences
c2 = MyCounter('Counter-2')
c3 = MyCounter('Counter-3')

counters = (c1, c2, c3)


def my_threading(consistently=False, infinite=False) -> None:
    """
    Run three counters consistently, infinite or parallel using threading
    :param consistently: boolean, run counters consistently
    :param infinite: boolean, run second counter infinite
    :return:
    """
    th_pause = 5
    th_inf = 10000
    for i, c in enumerate(counters):
        pause = th_inf if i == 1 and infinite else th_pause
        th = threading.Thread(target=c.count, args=(pause, ))
        th.start()
        if consistently:
            th.join()
