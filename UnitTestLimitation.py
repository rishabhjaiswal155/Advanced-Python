#Limitation of UnitTest:
#It always executes test methods in alphabetical order only.
#Also It is not possible to customize execution order.
#It is not possible to executes only particular specified test method.Default all test method executes.

import unittest
class UnitTestLimitation(unittest.TestCase):
    def test_methodC(self):
        print("test_methodC() executes...")
    def test_methodB(self):
        print("test_methodB() executes...")
    def test_methodA(self):  
        print("test_methodA() executes...")

unittest.main()
