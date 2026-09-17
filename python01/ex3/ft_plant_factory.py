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

def main():
	print("=== Plant Factory Output ===")
	r = Plant("Rose", 25.0, 30)
	o = Plant("Oak", 200.0, 365)
	c = Plant("Cactus", 5.0, 90)
	s = Plant("Sunflower", 80.0, 45)
	f = Plant("Fern", 15.0, 120)
	print("Created: ", end="")
	r.show()
	print("Created: ", end="")
	o.show()
	print("Created: ", end="")
	c.show()
	print("Created: ", end="")
	s.show()
	print("Created: ", end="")
	f.show()


if __name__=="__main__":
	main()