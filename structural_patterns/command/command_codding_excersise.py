"""
Implement the Account.process()  method to process different account commands.

The rules are obvious:

    success indicates whether the operation was successful

    You can only withdraw money if you have enough in your account

"""
from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False

    def deposit(self, bank_account):
        bank_account.balance += self.amount
        self.success = True

    def withdraw(self, bank_account):
        if (bank_account.balance - self.amount) > 0:
            bank_account.balance -= self.amount
            self.success = True
        else:
            self.success = False
        return self.success


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            command.deposit(self)
        elif command.action == Command.Action.WITHDRAW:
            command.withdraw(self)


def test_account_process():
    a = Account()
    cmd = Command(Command.Action.DEPOSIT, 100)
    a.process(cmd)

    assert 100 == a.balance
    assert cmd.success

    cmd = Command(Command.Action.WITHDRAW, 50)
    a.process(cmd)

    assert 50 == a.balance
    assert cmd.success

    cmd.amount = 150
    a.process(cmd)

    assert 50 == a.balance
    assert not cmd.success
