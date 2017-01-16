# -*- coding: utf-8 -*-
from pytest import raises
from watson.validators import abc


class TestBaseValidator(object):

    def test_call_error(self):
        with raises(TypeError):
            abc.Validator()
