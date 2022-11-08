class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    # We have to separate responsibility of class and extract it to other class
    # def save_to_file(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_to_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()


j = Journal()
j.add_entry("I ate today")
j.add_entry("I want to rest")
print(f'Journal entries: \n{j}')

filepath = '/tmp/journal.txt'
PersistenceManager.save_to_file(j, filepath)
with open(filepath) as fh:
    print(f'File entries:\n{fh.read()}')
