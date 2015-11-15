# -*- coding: utf-8 -*-


class NoEnoughFundsException(Exception):
    """Not Enough Funds"""


class BankAccount(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value < 0:
            raise NoEnoughFundsException

        self._balance = value

    balance = property(get_balance, set_balance)
