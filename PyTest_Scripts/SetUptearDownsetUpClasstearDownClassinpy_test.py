#Implementation of setUp,tearDown and setUpClass,tearDownClass method in pytest using Decorator.
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

def test_methodA(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodA executes...")

def test_methodB(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodB executes...")

