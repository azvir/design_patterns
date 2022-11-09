txt = 'Programing Languages'
part = ['<p>', txt, '</p>']
print(''.join(part))

words = ['GoLang', 'Python']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

# Let's implement it in OOP


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent+1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for el in self.elements:
            lines.append(el.__str(indent+1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


# ul = HtmlBuilder('ul')
ul = HtmlElement.create('ul')
# ul.add_child('li', 'Python')
# ul.add_child('li', 'GoLang')
ul.add_child_fluent('li', 'Python').add_child_fluent('li', 'GoLang')

print(ul)
