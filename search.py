def find_ngrams(word, n):
    word_perms = [word[i:] for i in range(n)]
    return zip(*word_perms)


def find_allngrams(word, min=1, max=None):
    grams = []
    for i in range(min - 1, max or len(word)):
        grams.append(''.join(find_ngrams(word, i + 1)[0]))

    return grams


class Phrase(str):

    def lower(self):
        return Phrase(super(Phrase, self).lower())

    def words(self):
        return self.split()
