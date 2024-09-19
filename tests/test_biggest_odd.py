from pyhton_task.biggestodd import biggest_odd
import unittest
import tasks


class Test_BiggestOdd(unittest.TestCase):

    def test_return_the_biggest_odd(self):
        tasks.biggest_odd("23956")


    def test_biggest_function_return_biggest_odd(self):
        max = tasks.biggest_odd("23956")
        self.assertEquals(max, 9)  # add assertion here


