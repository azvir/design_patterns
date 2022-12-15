class BitMap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading file {self.filename} bitmap')

    def draw(self):
        print(f'Drawing {self.filename} image')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = BitMap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('Above drawing image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    bm = BitMap('car.png')
    draw_image(bm)
    draw_image(bm)  # file loaded twice
    print()
    lbm = LazyBitmap('cat.png')
    draw_image(lbm)
    draw_image(lbm)
