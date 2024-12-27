import unittest
from TestCase1 import *
from TestCase2 import *
tc1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)
ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)
