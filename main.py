# -*- coding: utf-8 -*-
import unittest
from _ParametrizedTestCase import ParametrizedTestCase
from TestLoginPage import TestLoginPage
from TestReviewProductPage import TestReviewProductPage

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestLoginPage, param={'username': 'testuser_jim', 'password': '123456'}))
    suite.addTest(ParametrizedTestCase.parametrize(TestReviewProductPage, param=13))
    unittest.TextTestRunner(verbosity=2).run(suite)