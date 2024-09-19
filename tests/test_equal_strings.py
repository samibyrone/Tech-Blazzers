from pyhton_task.equal_strings import equal_string
import unittest


class Testequalstrings(unittest.TestCase):

    def test_for_equal_strings(self):
        word = "love"
        word2 = "evol"
        words = (word == word2)
        self.assertEqual(words, False)

    def test_for_equal_strings_is_equal_each_other(self):
        word = "love"
        word2 = "evol"
        words = (len(word) == len(word2))
        self.assertEqual(words, True)

    def test_for_equal_strings_is_not_equal_each_other(self):
        word = "love"
        word2 = "evol"
        words = (word) != (word2)
        self.assertEqual(words, True)
