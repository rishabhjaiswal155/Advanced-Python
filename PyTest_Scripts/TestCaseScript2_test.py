import pytest
@pytest.mark.run(order=3)
def test_methodC(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodC executes...")

@pytest.mark.run(order=1)
def test_methodA(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodA executes...")

@pytest.mark.run(order=2)
def test_methodB(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodB executes...")

#Customized the order of execution of test methods by installing pytest-ordering and using decorator @pytest.mark.run(order=n)