class Command:
	def execute(self):
		pass

class Copy(Command):
	def execute(self):
		print("Copying ...")

class Paste(Command):
	def execute(self):
		print("Pasting ...")

class Save(Command):
	def execute(self):
		print("Saving ...")

class Macro:
	def __init__(self):
		self.commands = []

	def add(self, command):
		self.commands.append(command)

	def run(self):
		for o in self.commands:
			o.execute()

def main():
	macro = Macro()
	macro.add(Copy())
	macro.add(Paste())
	macro.add(Save())
	macro.run()

if __name__ == "__main__":
	main()
