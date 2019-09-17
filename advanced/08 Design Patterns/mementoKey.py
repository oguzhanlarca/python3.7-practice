import pickle

class Originator:

	def __init__(self):
		self._state = None

	def create_memento(self):
		return pickle.dumps(vars(self))

	def set_memento(self, memento):
		previous_state = pickle.loads(memento)
		vars(self).clear
		vars(self).update(previous_state)

def main():
	originator = Originator()

	print(vars(originator))

	memento = originator.create_memento()
	
	originator._state = True

	print(vars(originator))

	originator.set_memento(memento)

	print(vars(originator))

if __name__ == "__main__":
	main()
