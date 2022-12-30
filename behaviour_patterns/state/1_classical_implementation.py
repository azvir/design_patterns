from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print('Switch already on...')

    def off(self, switch):
        print('Switch already off...')


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turning light on')
        switch.state = OnState()


class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        print('Turning light off')
        switch.state = OffState()


if __name__ == '__main__':
    sw = Switch()

    sw.on()

    sw.off()
    sw.off()
