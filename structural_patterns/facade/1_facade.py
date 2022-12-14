class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [''] * width * height

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    def __init__(self):
        b = Buffer()
        self.current_view = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_view]

    def get_char_at(self, index):
        return self.current_view.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.current_view.buffer.write('hello')
    ch = c.current_view.get_char_at(-1)
    print(ch)
    print(len(c.current_view.buffer.buffer))
