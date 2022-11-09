"""
Builder Coding Exercise

You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

    cb = CodeBuilder('Person').add_field('name', '""') \
                              .add_field('age', '0')
    print(cb)

The expected output of the above code is:

    class Person:
      def __init__(self):
        self.name = ""
        self.age = 0

Please observe the same placement of spaces and indentation.
"""


class Code:
    indent_size = 2

    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.attributes = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        i1 = ' ' * ((indent + 1) * self.indent_size)
        i2 = ' ' * ((indent + 2) * self.indent_size)
        if self.value is not None:
            lines.append('{}self.{} = {}'.format(i2, self.name, self.value))
        else:
            lines.append('{}class {}:'.format(i, self.name))
            if not self.attributes:
                lines.append('{}pass'.format(i1))

        if self.attributes:
            lines.append('{}def __init__(self):'.format(i1))
            for a in self.attributes:
                lines.append(str(a))
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = Code(root_name)

    def add_field(self, name, value):
        self.__root.attributes.append(
            Code(name, value)
        )
        return self

    def __str__(self):
        return str(self.__root)


def test_empty_class():
    cb = CodeBuilder('Foo')
    assert __preprocess(str(cb)) == 'class Foo:\n  pass'


def test_person_class():
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', 0)
    expected = """\
class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0\
"""
    assert __preprocess(str(cb)) == expected


def test_employee_class():
    cb = CodeBuilder('Employee').add_field('name', '""').add_field('position', '""').add_field('annual_income', '0')
    expected = """\
class Employee:
  def __init__(self):
    self.name = \"\"
    self.position = \"\"
    self.annual_income = 0\
"""
    assert __preprocess(str(cb)) == expected


def __preprocess(s=''):
    return s.strip().replace('\r\n', '\n')
