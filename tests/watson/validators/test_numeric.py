# -*- coding: utf-8 -*-
from pytest import raises
from watson.validators.numeric import Range


class TestRange(object):

    def test_does_not_meet_range(self):
        with raises(ValueError):
            validator = Range(1, 10)
            validator(11)

    def test_does_meet_range(self):
        validator = Range(1, 10)
        validator(5)
        validator(5.4)
        validator('6')

    def test_no_min_or_max(self):
        with raises(ValueError):
            Range()

    def test_min_greater_max(self):
        with raises(ValueError):
            Range(5, 1)
