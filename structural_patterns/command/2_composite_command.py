from abc import ABC
from enum import Enum

import pytest


class BankAccount:
    WITHDRAW_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        return True

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.WITHDRAW_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        ...

    def undo(self):
        ...


class CommandBankAccount(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, bank_account: BankAccount, action: Action, amount: int):
        super().__init__()
        self.bank_account = bank_account
        self.action = action
        self.amount = amount

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


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: list[Command]):
        super().__init__()
        for item in items:
            self.append(item)

    def invoke(self):
        for cmd in self:
            cmd.invoke()

    def undo(self):
        for cmd in self:
            cmd.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc, to_acc, amount):
        super().__init__(
            [
                CommandBankAccount(from_acc, CommandBankAccount.Action.WITHDRAW, amount),
                CommandBankAccount(to_acc, CommandBankAccount.Action.DEPOSIT, amount)
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


def test_transfer_by_composite():
    ba1 = BankAccount(100)
    ba2 = BankAccount()
    wc = CommandBankAccount(ba1, CommandBankAccount.Action.WITHDRAW, 100)
    dc = CommandBankAccount(ba2, CommandBankAccount.Action.DEPOSIT, 100)
    composite_cmd = CompositeBankAccountCommand([wc, dc])
    composite_cmd.invoke()
    assert ba1.balance == 0
    assert ba2.balance == 100
    composite_cmd.undo()
    assert ba1.balance == 100


@pytest.mark.xfail(reason='CompositeBankAccountCommand has bug')
def test_fail_transfer_by_composite():
    ba1 = BankAccount(100)
    ba2 = BankAccount()
    wc = CommandBankAccount(ba1, CommandBankAccount.Action.WITHDRAW, 1000)
    dc = CommandBankAccount(ba2, CommandBankAccount.Action.DEPOSIT, 1000)
    composite_cmd = CompositeBankAccountCommand([wc, dc])
    composite_cmd.invoke()
    assert ba1.balance == 100
    assert ba2.balance == 0


def test_better_transfer():
    ba1 = BankAccount(100)
    ba2 = BankAccount()

    amount = 1000

    transfer = MoneyTransferCommand(ba1, ba2, amount)
    transfer.invoke()
    print('ba1:', ba1, 'ba2:', ba2)
    assert ba1.balance == 100
    assert ba2.balance == 0
    transfer.undo()
    print('ba1:', ba1, 'ba2:', ba2)
    assert ba1.balance == 100
    assert ba2.balance == 0
    assert not transfer.success
