class Account:
	def __init__(self,name,balance,min_balance):
		self.name=name
		self.balance=balance
		self.min_balance=min_balance
		
	def deposit(self,amount):
		self.balance=self.balance+amount
		
	def withdraw(self,amount):
		if self.balance-amount>=self.min_balance:
			self.balance=self.balance-amount
		else:
			print("Insufficient Funds to Withdraw!!")
		
	def printstatement(self):
		print("{}'s account balance is:{}".format(self.name,self.balance))
	
class CurrentAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,min_balance=-1000)
	
	def __str__(self):
		return "{}'s account balance is:{}".format(self.name,self.balance)
		
class SavingsAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,min_balance=0)
	
	def __str__(self):
		return "{}'s account balance is:{}".format(self.name,self.balance)
		
ca=CurrentAccount('Rishabh',10000)
ca.printstatement()
ca.deposit(10000)
ca.printstatement()
ca.withdraw(5000)
ca.printstatement()
ca.withdraw(15900)
ca.printstatement()
print(ca)

sa=SavingsAccount('Rishabh',20000)
sa.deposit(10000)
sa.printstatement()
sa.withdraw(15000)
print(sa)
sa.withdraw(15500)
print(sa)