import unittest
from pyhton_task.sample_task import TestKeyCube


class TestKeyCube(unittest.TestCase):

    def test_that_function_exist(self):
        tasks.get_key_cube([1, 2, 3, 4, 5])

    def test_that_function_return_dict(self):
        actual = tasks.get_key_cube([1, 2, 3, 4, 5])
        expected = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(actual, expected)
