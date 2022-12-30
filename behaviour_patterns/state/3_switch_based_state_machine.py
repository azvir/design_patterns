from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    code = '1234'
    state = State.LOCKED

    entry = ''

    while True:
        match state:
            case State.LOCKED:
                entry += input(entry)

                if entry == code:
                    state = State.UNLOCKED

                if not code.startswith(entry):
                    state = State.FAILED

            case State.FAILED:
                print('\nFailed')
                entry = ''
                state = State.LOCKED
            case State.UNLOCKED:
                print('\nUnlocked')
                break
