from collections import Counter
import sys
import collections

class Database(object):
	def __init__(self):		
		self.transactions = [] # represents changes from the last transaction history	
		self.db = {} # database
		self.counter = Counter() # used for function numequalto() 
        
   	def begin(self):		
		self.transactions.insert(0, {}) # creates a new transaction history
		

	def get(self, name):		
		if name in self.db:
			print '\n> '+self.db[name]
		else:
			print '\n> NULL'

	def write(self, name, value):
		if name in self.db:
			self.counter[self.db[name]] -= 1
		self.db[name] = value
		self.counter[value] += 1


	def set(self, name, value):					
		self.__save_state(name)
		self.write(name, value)

	def __save_state(self, name):
		if self.transactions: # update the changed item in the transaction		
			if name in self.db and name not in self.transactions[0]:
				self.transactions[0][name] = self.db[name]
				
			if name not in self.db:
				self.transactions[0][name] = None	
	
	def __unset(self, name):
		self.counter[self.db[name]] -= 1
		del self.db[name]

	def unset(self, name):			
		self.__save_state(name)	
		self.__unset(name)
	

	def rollback(self):		
		if self.transactions:
			state = self.transactions.pop(0)
			for key in state:
				if state[key] == None:
					self.__unset(key)
				else:
					self.write(key, state[key])			
		else:
			print "\n> NO TRANSACTION"


	def commit(self):		
		if not self.transactions:
			print "\n> NO TRANSACTION"
		self.transactions = [] # clear the transaction history
	

	def numequalto(self, value):		
		print '\n> ',self.counter[value]



			
if __name__ == "__main__":
	db = Database()
	line = sys.stdin.readline().strip()
	while line != 'END':
		args = line.split(' ')
		commands = ['BEGIN', 'ROLLBACK', 'COMMIT', 'SET', 'GET', 'UNSET', 'NUMEQUALTO']	
		
		if args[0] in commands:			
			command = getattr(Database, args[0].lower());			
			command(db,*args[1:])				
		line = sys.stdin.readline().strip()

	

