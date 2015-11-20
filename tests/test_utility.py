# -*- coding: utf-8 -*-
from datetime import date
from utility import is_last_of_month


def test_is_last_of_month():
    d = date(2011, 11, 30)
    assert is_last_of_month(d), "%s" % d


def test_is_last_of_month_not():
    d = date(2011, 11, 29)
    assert not is_last_of_month(d), "%s" % d
