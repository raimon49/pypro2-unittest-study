# -*- coding: utf-8 -*-
import urllib2


class NoEnoughFundsException(Exception):
    """Not Enough Funds"""


class DummyFailException(Exception):
    """This is dummy"""


class BankAccount(object):

    def __init__(self):
        self._balance = 0

    def must_fail(self):
        raise DummyFailException('This is dummy')

    def is_authorized(self):
        not_authorized = False
        try:
            res = urllib2.urlopen('https://example.com/auth')
            text = res.read()
            if res.code == 200 and text is not None:
                return True
        except urllib2.HTTPError, e:
            pass

        return not_authorized

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
