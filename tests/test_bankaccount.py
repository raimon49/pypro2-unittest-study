# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock, MagicMock, PropertyMock


def mocked_response(status_code=200):
    """
    Return mocked response instance

        >>> mocked_response(status_code=404).code == 404
        True
        >>> mocked_response(status_code=404).code == 200
        False
        >>> mocked_response(status_code=404).read() == 'mocked body'
        True
    """
    code = PropertyMock()
    code.return_value = status_code

    response = MagicMock()
    response.read.return_value = 'mocked body'
    type(response).code = code

    return response


class TestBankAccount(unittest.TestCase):

    def _getTarget(self):
        from bankaccount import BankAccount
        return BankAccount

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_must_fail(self):
        target = self._makeOne()
        from bankaccount import DummyFailException
        with self.assertRaises(DummyFailException):
            target.must_fail()

        # メソッドの差し替え
        m = Mock()
        m.returnValue = True
        target.must_fail = m
        self.assertFalse(m.called)
        self.assertTrue(target.must_fail())
        self.assertTrue(m.called)

    @patch('urllib2.urlopen')
    def test_is_authorized(self, urlopen):
        target = self._makeOne()

        urlopen.return_value = mocked_response()
        self.assertTrue(target.is_authorized())

        urlopen.return_value = mocked_response(status_code=403)
        self.assertFalse(target.is_authorized())

    def test_construct(self):
        target = self._makeOne()
        self.assertEqual(target._balance, 0)

    def test_deposit(self):
        target = self._makeOne()
        target.deposit(100)
        self.assertEqual(target._balance, 100)

    def test_withdraw(self):
        target = self._makeOne()
        target._balance = 100
        target.withdraw(20)
        self.assertEqual(target._balance, 80)

    def test_get_balance(self):
        target = self._makeOne()
        target._balance = 500
        self.assertEqual(target.get_balance(), 500)

    def test_set_balance(self):
        target = self._makeOne()
        target.set_balance(500)
        self.assertEqual(target._balance, 500)

    def test_set_balance_not_enough_funds(self):
        target = self._makeOne()
        from bankaccount import NoEnoughFundsException
        with self.assertRaises(NoEnoughFundsException):
            target.set_balance(-1)
