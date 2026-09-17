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
	r = Plant("Rose", 25.0, 30)
	print("=== Garden Plant Growth ===")
	r.show()
	growth = r.height
	for i in range(1, 8):
		print(f"=== Day {i} ===")
		r.grow()
		r.age()
		r.show()
	growth = r.height - growth
	print(f"Growth this week: {growth:.1f}cm")

if __name__=="__main__":
	main()