#Implementation of setUp method in pytest using Decorator.
import pytest #module
@pytest.fixture() #decorator for implementing setUp()
def setUp(): #name can be anything
	print("setUp method executes...")
	
def test_methodA(setUp): #passing the name of setUp() as argument
	print("test_methodA executes...")

def test_methodB(setUp): #passing the name of setUp() as argument
	print("test_methodB executes...")

