#Implementation of setUp and tearDown method in pytest using Decorator.
import pytest #module
@pytest.yield_fixture() #decorator for implementing both setUp() and tearDown()
def setUptearDown(): #name can be anything
	print("setUp method executes...")
	yield
	print("tearDown method executes...")
	
def test_methodA(setUptearDown): #passing the name of setUptearDown() as argument
	print("test_methodA executes...")

def test_methodB(setUptearDown): #passing the name of setUptearDown() as argument
	print("test_methodB executes...")

