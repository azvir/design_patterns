"""

Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores just one
 numeric value, but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum
 that returns a sum of all the values that the object contains.
  Please ensure that there is only a single method that realizes the property sum, not multiple methods.

Here is a sample unit test:

    class FirstTestSuite(unittest.TestCase):
        def test(self):
            single_value = SingleValue(11)
            other_values = ManyValues()
            other_values.append(22)
            other_values.append(33)
            # make a list of all values
            all_values = ManyValues()
            all_values.append(single_value)
            all_values.append(other_values)
            self.assertEqual(all_values.sum, 66)
"""

from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        sum_ = 0
        for s in self:
            for i in s:
                sum_ += i
        return sum_


class SingleValue(ValueContainer):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    ...


def test():
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    assert all_values.sum == 66
