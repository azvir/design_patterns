from abc import ABC
from enum import Enum


class BandAccount:
    WITHDRAW_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        return True

    def withdraw(self, amount):
        if self.balance - amount >= BandAccount.WITHDRAW_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def invoke(self):
        ...

    def undo(self):
        ...


class CommandBandAccount(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, bank_account: BandAccount, action: Action, amount: int):
        self.bank_account = bank_account
        self.action = action
        self.amount = amount
        self.success = False

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.success = self.bank_account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.bank_account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action == self.Action.DEPOSIT:
                self.success = self.bank_account.withdraw(self.amount)
            elif self.action == self.Action.WITHDRAW:
                self.success = self.bank_account.deposit(self.amount)


def test_deposit_100_usd():
    ba = BandAccount()
    cmd = CommandBandAccount(ba, CommandBandAccount.Action.DEPOSIT, 100)
    cmd.invoke()
    assert "Balance = 100" == str(ba)


def test_undo_deposited_100_usd():
    ba = BandAccount()
    cmd = CommandBandAccount(ba, CommandBandAccount.Action.DEPOSIT, 100)
    cmd.invoke()
    assert "Balance = 100" == str(ba)
    cmd.undo()
    assert "Balance = 0" == str(ba)


def test_cannot_perform_illegal_cmd():
    ba = BandAccount()
    cmd = CommandBandAccount(ba, CommandBandAccount.Action.WITHDRAW, 1000)
    cmd.invoke()
    assert "Balance = 0" == str(ba)
    cmd.undo()
    assert "Balance = 0" == str(ba)
