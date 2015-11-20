# -*- coding: utf-8 -*-
from datetime import timedelta


def is_last_of_month(d):
    return (d + timedelta(1)).day == 1
