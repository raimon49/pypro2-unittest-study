# -*- coding: utf-8 -*-
from datetime import date
from testfixtures import Replacer, test_datetime
from utility import is_last_of_month, is_last_of_month_now


def test_is_last_of_month():
    d = date(2011, 11, 30)
    assert is_last_of_month(d), "%s" % d


def test_is_last_of_month_not():
    d = date(2011, 11, 29)
    assert not is_last_of_month(d), "%s" % d


def test_is_last_of_month_now():
    with Replacer() as r:
        r.replace('utility.datetime', test_datetime(2011, 11, 30))
        assert is_last_of_month_now()
