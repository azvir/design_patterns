"""
A combination lock is a lock that opens after the right digits have been entered.
 A lock is preprogrammed with a combination (e.g., 12345 )
 and the user is expected to enter this combination to unlock the lock.

The lock has a Status field that indicates the state of the lock. The rules are:

    If the lock has just been locked (or at startup), the status is LOCKED.

    If a digit has been entered, that digit is shown on the screen.
     As the user enters more digits, they are added to Status.

    If the user has entered the correct sequence of digits, the lock status changes to OPEN.

    If the user enters an incorrect sequence of digits, the lock status changes to ERROR.

Please implement the CombinationLock  class to enable this behavior. Be sure to test both correct and incorrect inputs.

"""


class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.code = ''.join(map(str, combination))

    def reset(self):
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        if self.status == 'LOCKED':
            self.status = str(digit)
            return
        if self.status.isdigit():
            self.status += str(digit)
            if self.status == self.code:
                self.status = 'OPEN'
                return
            if not self.code.startswith(self.status):
                self.status = 'ERROR'


def test_success():
    cl = CombinationLock([1, 2, 3, 4, 5])
    assert 'LOCKED' == cl.status
    cl.enter_digit(1)
    assert '1' == cl.status
    cl.enter_digit(2)
    assert '12' == cl.status
    cl.enter_digit(3)
    assert '123' == cl.status
    cl.enter_digit(4)
    assert '1234' == cl.status
    cl.enter_digit(5)
    assert 'OPEN' == cl.status


def test_failure():
    cl = CombinationLock([1, 2, 3])
    assert 'LOCKED' == cl.status
    cl.enter_digit(1)
    assert '1' == cl.status
    cl.enter_digit(2)
    assert '12' == cl.status
    cl.enter_digit(5)
    assert 'ERROR' == cl.status
