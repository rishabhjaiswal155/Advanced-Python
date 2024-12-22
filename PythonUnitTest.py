#Python Unit Testing
import unittest #module for Python UnitTest
class TestCaseDemo(unittest.TestCase): #extending from unittest.TestCase class
    @classmethod #class level method (executes only one time.)
    def setUpClass(cls):
        print("setUpClass method executes...")
       
    def setUp(self): #instance method (executes for each test_method)
        print("setUp method executes....")
          
    def test_method1(self): #test_method
        print("test_method1 method executes...")
        #print(10/0)
    
    def test_method2(self): #test_method
        print("test_method2 method executes...")
    
    def tearDown(self): #instance method (executes for each test_method)
        print("tearDown method executes...")
    
    @classmethod #class level method (executes only one time.)
    def tearDownClass(cls):
        print("tearDownClass method executes...")

unittest.main() #calling to above class
