from abc import ABCMeta
from abc import abstractmethod

from google.appengine.api import search


class TokenFilter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, token_string):
        return token_string


class EdgeNGramTokenFilter(TokenFilter):

    def __init__(self, min_gram_size=1, max_gram_size=None):
        self.min_gram_size = min_gram_size
        self.max_gram_size = max_gram_size

    def create(self, token_string):
        edge_ngrams = self._find_edge_ngrams(token_string,
                                             self.min_gram_size,
                                             self.max_gram_size)

        return ' '.join(edge_ngrams)

    def _find_ngrams(self, word, n):
        word_perms = [word[i:] for i in range(n)]
        return zip(*word_perms)

    def _find_edge_ngrams(self, word, min=1, max=None):
        grams = []
        for i in range(min - 1, max or len(word)):
            grams.append(''.join(self._find_ngrams(word, i + 1)[0]))

        return grams


class TextField(search.TextField):
    """A Field that has text content.

    The following example shows a text field named signature in Polish:
    TextField(name='signature', value='brzydka pogoda', language='pl')

    The following example shows a text field named signature and using a custom
    token filter:
    TextField(name='title', value='horses', search.EdgeNGramTokenFilter())
    """
    def __init__(self, name, value=None, language=None, token_filter=None):
        """Initializer.

        Args:
        name: The name of the field.
        value: A str or unicode object containing text.
        language: The code of the language the value is encoded in.
        token_filter: The TokenFilter class to perform custom token filtering
                      before storing the value

        Raises:
        TypeError: If value is not a string.
        ValueError: If value is longer than allowed.
        """
        value = token_filter.create(value)

        super(TextField, self).__init__(name,
                                        search.search._ConvertToUnicode(value),
                                        language)
