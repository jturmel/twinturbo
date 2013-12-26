import unittest
import search


class SearchTest(unittest.TestCase):
    def test_find_allngrams(self):
        word = 'horses'
        result = ['ho', 'hor', 'hors', 'horse', 'horses']

        self.assertEqual(search.find_allngrams(word, 2), result)

    def test_phrase(self):
        p = 'Once upon a time'
        phrase = search.Phrase(p)
        result = ['once', 'upon', 'a', 'time']

        self.assertEqual(phrase.lower().words(), result)
