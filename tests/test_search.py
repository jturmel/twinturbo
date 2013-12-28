import unittest
import search


class SearchTest(unittest.TestCase):
    def test_find_allngrams(self):
        word = 'horses'
        result = ['ho', 'hor', 'hors', 'horse', 'horses']

        self.assertEqual(search.find_allngrams(word, 2), result)
