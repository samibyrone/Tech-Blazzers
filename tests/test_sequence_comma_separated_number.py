import unittest

from pyhton_task.sequence_comma_separated_number import sequence_separated_number

class Test_separated_sequence_numbers(unittest.TestCase):

    def test_number_function_exist(self):
        index = "34,67,55,33,12,98"
        expected = ['34','67','55','33','12','98']

    def test_that_function_generate_string_to_list_and_tuple(self):
        index = "34, 67, 55, 33, 12, 98"
        display_list = ['34', '67', '55', '33', '12', '98']
        tuple_display_list = ('34', '67', '55', '33', '12', '98')
        self.assertEqual(index, (display_list, tuple_display_list), "you got it right.")
