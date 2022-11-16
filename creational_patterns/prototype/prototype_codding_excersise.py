"""
Given the definitions shown in code, you are asked to implement Line.deep_copy()
to perform a deep copy of the given Line object.
This method should return a copy of a Line that contains copies of its start/end points.

Note: please do not confuse deep_copy() with __deepcopy__()!
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        cp_start = Point(self.start.x, self.start.y)
        cp_end = Point(self.end.x, self.end.y)
        return Line(cp_start, cp_end)


def test_deep_copy_return_other_object():
    line_proto = Line(start=Point(2, 2), end=Point(5, 5))
    line = line_proto.deep_copy()
    line_proto.start.x = line_proto.start.y = line_proto.end.x = line_proto.end.y = 0
    assert 2 == line.start.x
    assert 2 == line.start.y
    assert 5 == line.end.x
    assert 5 == line.end.y
