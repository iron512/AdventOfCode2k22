class Monkey:
	def __init__(self, items, operation, test, true, false):
		self.items = items
		self.operation = operation
		self.test = test
		self.true = true
		self.false = false
		self.examined = 0

	def __str__(self):
		return "Items: [" + ", ".join(str(val) for val in self.items) + "], examined:" + str(self.examined) + " items"

	def compute_operation(self, value):
		sub = str(self.operation).replace("old", str(value))
		results = {}
		exec(sub, None, results)
		return results['new']

	def add_item(self, item):
		self.items.append(item)

	def launch(self, monkeys):
		for obj in self.items:
			inspect = self.compute_operation(obj)
			boredom = int(inspect/3)
			launch = self.true if boredom % self.test == 0 else self.false
			monkeys[launch].add_item(boredom)
			self.examined += 1
		self.items = []


def main(test):
	rows = open("input_easy.txt").read().split("\n\n")
	if not test:
		rows = open("input.txt").read().split("\n\n")

	monkeys = []
	for row in rows:
		attributes = row.split("\n")
		objects = [int(obj) for obj in attributes[1].split(":")[1].split(",")]
		operation = attributes[2].strip().split(":")[1].strip()
		test = int(attributes[3].strip().split(" ")[3])
		true = int(attributes[4].strip().split(" ")[5])
		false = int(attributes[5].strip().split(" ")[5])

		monkeys.append(Monkey(objects, operation, test, true, false))

	# do a round
	for i in range(20):
		for monkey in monkeys:
			monkey.launch(monkeys)

	# for monkey in monkeys:
	# 	print(monkey)
	examination_results = sorted([monkey.examined for monkey in monkeys], reverse=True)
	print("The most examinative monkeys product are:", examination_results[0]*examination_results[1])


if __name__ == '__main__':
	main(False)
