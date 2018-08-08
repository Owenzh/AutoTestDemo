# -*- coding: utf-8 -*-
from _ParametrizedTestCase import ParametrizedTestCase

class TestReviewProductPage(ParametrizedTestCase):
    def test_product_open(self):
        print 'param =', self.param
        self.assertEqual(1, 1)
 
    def test_product_count(self):
        self.assertEqual(2, 2)