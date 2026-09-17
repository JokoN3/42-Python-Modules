class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
	print("=== Garden Plant Registry ===")
	rose = Plant("Rose", 25, 30)
	rose.show()
	sunflower = Plant("Sunflower", 80, 45)
	sunflower.show()
	cactus = Plant("Cactus", 15, 120)
	cactus.show()


if __name__=="__main__":
	main()