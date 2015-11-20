# -*- coding: utf-8 -*-
import unittest


class DummyRequest(object):

    def __init__(self, params):
        self.params = params


class DummyService(object):

    def some_method(self, **kwargs):
        return kwargs


class TestIt(unittest.TestCase):

    def test_it(self):
        from myview import MyView
        request = DummyRequest(params={'a': 1})
        target = MyView(request)
        target.someservice_cls = DummyService
        request = target.index()
        self.assertEqual(target.render_context['result'], {'a': 1})
