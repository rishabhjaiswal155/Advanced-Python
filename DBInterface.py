from abc import *
class DBInterface(ABC):
	@abstractmethod
	def connect(self):
		pass
	@abstractmethod
	def disconnect(self):
		pass

class Oracle(DBInterface):
	def connect(self):
		print("Oracle DataBase Connected....")
	
	def disconnect(self):
		print("Oracle DataBase Disconnected....")
		
class MySql(DBInterface):
	def connect(self):
		print("MySql DataBase Connected....")
	
	def disconnect(self):
		print("MySql DataBase Disconnected....")
		
o=Oracle()
o.connect()
o.disconnect()

	
m=MySql()
m.connect()
m.disconnect()
