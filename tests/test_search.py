import unittest
import search


class SearchTest(unittest.TestCase):

    def test_TextField1(self):
        token_filter = search.EdgeNGramTokenFilter(min_gram_size=1)
        field = search.TextField(name='title',
                                 value='horses',
                                 token_filter=token_filter)

        self.assertEqual(field.value, 'h ho hor hors horse horses')

    def test_TextField2(self):
        token_filter = search.EdgeNGramTokenFilter(min_gram_size=2)
        field = search.TextField(name='title',
                                 value='buggies',
                                 token_filter=token_filter)

        self.assertEqual(field.value, 'bu bug bugg buggi buggie buggies')

    def test_TextField3to5(self):
        token_filter = search.EdgeNGramTokenFilter(min_gram_size=3,
                                                   max_gram_size=5)
        field = search.TextField(name='title',
                                 value='buggies',
                                 token_filter=token_filter)

        self.assertEqual(field.value, 'bug bugg buggi')
