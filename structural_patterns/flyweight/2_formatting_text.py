class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(self.plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)


class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range_ = self.TextRange(start, end)
        self.formatting.append(range_)
        return range_

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                result.append(c.upper() if r.covers(i) and r.capitalize else c)
        return ''.join(result)


if __name__ == '__main__':
    text = 'This is a brave new world'
    ft = FormattedText(text)
    print('Original text')
    print('  ' + str(ft))
    print('Capitalize 10-15 letters')
    ft.capitalize(10, 15)
    print('  ' + str(ft))

    bft = BetterFormattedText(text)
    print('Capitalize 16-19 letters')
    bft.get_range(16, 19).capitalize = True
    print('  ' + str(bft))
