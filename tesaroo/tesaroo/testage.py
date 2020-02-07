from django.test import TestCase
from .staticfunctions import add,div
class test_ThisOne(TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    
    def test_divide(self):
        self.assertRaises(TypeError,div,4,0)
