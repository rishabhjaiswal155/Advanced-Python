#Implementation of common setUp,tearDown and setUpClass,tearDownClass activities in pytest using conftest.py file:
import pytest #module
@pytest.yield_fixture(scope='module') #decorator for implementing both setUpClass() and tearDownClass()
def setUpClasstearDownClass(): #name can be anything
	print("setUpClass method executes...")
	yield
	print("tearDownClass method executes...")
	
@pytest.yield_fixture() #Decorator for implementing both setUp() and tearDown()
def setUptearDown():
	print("setUp method executes...")
	yield
	print("tearDown method executes...")
