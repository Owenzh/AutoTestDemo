# -*- coding: utf-8 -*-
from _ParametrizedTestCase import ParametrizedTestCase

class TestLoginPage(ParametrizedTestCase):
    def test_login_info(self):
        print 'param =', self.param['username']
        self.assertEqual('testuser_jim', self.param['username'])
 
    def test_login_click(self):
        self.assertEqual(2, 2)