class GraphicalObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicalObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicalObject):
    @property
    def name(self):
        return 'Square'


if __name__ == "__main__":
    drawing_item = GraphicalObject()
    drawing_item._name = 'My Drawing'
    drawing_item.children.append(Square('Blue'))
    drawing_item.children.append(Circle('Red'))

    group = GraphicalObject()
    group.children.append(Square('Yellow'))
    group.children.append(Circle('Green'))
    drawing_item.children.append(group)

    print(drawing_item)
