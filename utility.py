# -*- coding: utf-8 -*-
from datetime import timedelta, datetime


def is_last_of_month(d):
    return (d + timedelta(1)).day == 1


def is_last_of_month_now():
    return is_last_of_month(datetime.now())
