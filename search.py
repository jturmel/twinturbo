def find_ngrams(word, n):
    word_perms = [word[i:] for i in range(n)]
    return zip(*word_perms)


def find_allngrams(word, min=1, max=None):
    grams = []
    for i in range(min - 1, max or len(word)):
        grams.append(''.join(find_ngrams(word, i + 1)[0]))

    return grams


#class NGramField(search.TextField):
    #"""A Field that has text content and will will be stored as n-grams
    #starting at 2

    #The following example shows a text field named first_name:
    #TextField(name='first_name', value='Robert')

    #The value will be stored as 'Ro Rob Robe Rober Robert'
    #"""

    #def __init__(self, name, value=None):
        #"""Initializer.

        #Args:
        #name: The name of the field.
        #value: A str or unicode object containing text.

        #Raises:
        #TypeError: If value is not a string.
        #ValueError: If value is longer than allowed.
        #"""
        #value = find_allngrams(value, 2)
        #super(NGramField, self).__init__(name, value)
