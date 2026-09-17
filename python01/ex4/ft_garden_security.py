class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.oldness = age
	def show(self):
		print(f"{self.name}: {self.height:.1f}cm, {self.oldness} days old")
	def grow(self):
		self.height += 0.8
	def age(self):
		self.oldness += 1
	def get_height(self):
		return self.height
	def get_age(self):
		return self.oldness
	def set_age(self, new_age):
		if new_age >= 0:
			self.oldness = new_age
			print(f"Age updated: {self.oldness} days")
		else:
			print(f"{self.name}: Error, age can't be negative")
			print("Age update rejected")
	def set_height(self, new_height):
		if new_height >= 0:
			self.height = new_height
			print(f"Height updated: {self.height}cm")
		else:
			print(f"{self.name}: Error, height can't be negative")
			print("Height update rejected")



def main():
	r = Plant("Rose", 15, 10)
	print("=== Garden Security System ===")
	print("Plant created: ", end="")
	r.show()
	print()
	r.set_height(25)
	r.set_age(30)
	print()
	r.set_height(-1)
	r.set_age(-1)
	print()
	print("Current state: ", end="")
	r.show()
if __name__=="__main__":
	main()