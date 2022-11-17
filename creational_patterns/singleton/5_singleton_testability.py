from pytest import fixture


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}

        # !!! file not exist
        f = open('capitals.txt', 'r')
        lines = f.readline()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())
        f.close()


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result


class DummyDB:
    population = {
        'alpha': 1,
        'betta': 2,
        'gamma': 3,
    }

    def get_population(self, name):
        return self.population[name]


class ConfigurableRecordFinder:
    def __init__(self, db=Database()):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


def test_is_singleton():
    db1 = Database()
    db2 = Database()
    assert db1 == db2


def test_singleton_total_population():
    rf = SingletonRecordFinder()
    names = ['Seoul', 'Mexico City']
    tp = rf.total_population(names)
    assert tp == (17500000 + 1740000)


def test_dependent_database():
    ddb = DummyDB()
    crf = ConfigurableRecordFinder(db=ddb)
    assert 3 == crf.total_population(['alpha', 'betta'])

