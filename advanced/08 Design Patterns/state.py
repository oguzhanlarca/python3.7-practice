class AtmState():

	name = "state"
	allowed = []

	def goNext(self, state):
		if state.name in self.allowed:
			print("Current State: ", self, " switched to: ", state.name)
			

		else:
			print("Current State: ", self, " switching to: ", state.name, " not possible!")

	def __str__(self):
		return self.name

class Off(AtmState):

	name = "off"
	allowed = ['on']

class On(AtmState):

		

class ATM():
	
	def __init__(self):
			

	def setState(self, state):
		

def main():

	

if __name__ == "__main__":
	main()

