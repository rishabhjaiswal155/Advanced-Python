def test_methodC(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodC executes...")

def test_methodA(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodA executes...")

def test_methodB(setUpClasstearDownClass,setUptearDown): #passing the name of both setUpClasstearDownClass() and setUptearDown() as argument
	print("test_methodB executes...")

#default order of execution for test methods in pytest is from top to bottom.