class Word:
    def __init__(self, text, capitalize=False):
        self.text = text
        self.capitalize = capitalize

    def __str__(self):
        return self.text.upper() if self.capitalize else self.text


class Sentence:
    def __init__(self, plain_text):
        self.words = [Word(text) for text in plain_text.split(' ')]

    def __getitem__(self, key):
        return self.words.__getitem__(key)

    def __str__(self):
        return ' '.join(map(str, self.words))


def test_formatting_second_word_in_sentence():
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    assert str(sentence) == 'hello WORLD'
    