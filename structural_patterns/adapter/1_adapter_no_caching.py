class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print('.', end='')


# ^^ you are given this

# vv   my code

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    count = 0

    def __init__(self, line: Line):
        super().__init__()
        self.count += 1

        print(f'{self.count}: Generating points for line '
              f'[{line.start.x}, {line.start.y}] -> [{line.end.x}, {line.end.y}]')
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(bottom, top):
                self.append(Point(left, y))
        elif top - bottom == 0:
            for x in range(left, right):
                self.append(Point(x, bottom))


def draw(rcs_):
    print('\n\n--- Drawing some stuff ----\n')
    for rc in rcs_:
        for line in rc:
            points = LineToPointAdapter(line)
            for p in points:
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(4, 4, 5, 5)
    ]
    draw(rcs)
