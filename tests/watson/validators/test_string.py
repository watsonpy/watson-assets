# -*- coding: utf-8 -*-
from pytest import raises
from watson.validators.string import Length, Required, RegEx, Csrf


class TestLength(object):

    def test_invalid_min_greater_than_max(self):
        with raises(ValueError):
            Length(min=10, max=9)

    def test_none_value(self):
        validator = Length(min=1, max=2)
        with raises(ValueError):
            validator(None)

    def test_doesnt_meet_min_requirement(self):
        with raises(ValueError):
            validator = Length(min=10)
            validator('Test')

    def test_meets_min_requirement(self):
        validator = Length(min=1)
        assert validator('Test')

    def test_doesnt_meet_max_requirement(self):
        with raises(ValueError):
            validator = Length(max=10)
            validator('This is a test')

    def test_meets_max_requirement(self):
        validator = Length(max=10)
        assert validator('Test')

    def test_exact_value(self):
        validator = Length(min=4, max=4)
        assert validator('Test')

    def test_between_values(self):
        validator = Length(min=1, max=10)
        assert validator('Test')


class TestRequired(object):

    def test_has_value(self):
        validator = Required()
        assert validator('Test')

    def test_has_no_value(self):
        with raises(ValueError):
            validator = Required()
            validator('')


class TestRegex(object):

    def test_match_regex(self):
        validator = RegEx('Test')
        validator('Test')

    def test_no_match(self):
        with raises(ValueError):
            validator = RegEx('Test')
            validator('Fail')


class TestCsrf(object):

    def test_create(self):
        validator = Csrf(token='1234')
        assert validator.token == '1234'

    def test_invalid_match(self):
        validator = Csrf(token='1234')
        with raises(ValueError):
            validator('12345')
