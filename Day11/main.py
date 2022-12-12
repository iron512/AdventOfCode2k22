import copy


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
		results = {'old': value}
		exec(self.operation, None, results)
		return results['new']

	def add_item(self, item):
		self.items.append(item)

	def launch(self, monkeys, worry=True, divisor=1):
		for obj in self.items:
			inspect = self.compute_operation(obj)
			if worry:
				boredom = int(inspect/3)
			else:
				boredom = inspect % divisor
			launch = self.true if boredom % self.test == 0 else self.false
			monkeys[launch].add_item(boredom)
			self.examined += 1
		self.items = []


def main(test=False):
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

	more_annoying = copy.deepcopy(monkeys)
	for i in range(20):
		# do a round
		for monkey in monkeys:
			monkey.launch(monkeys)

	checks = [monkey.test for monkey in more_annoying]
	multiple = 1
	for value in checks:
		multiple *= value

	# PART 2
	for i in range(1,10001):
		# do a round
		if i % 100 == 0:
			print("Completed at", int(i / 100), "%")
		for monkey in more_annoying:
			monkey.launch(more_annoying, False, multiple)

	# for monkey in monkeys:
	# 	print(monkey)
	examination_results_20 = sorted([monkey.examined for monkey in monkeys], reverse=True)
	examination_results_10k = sorted([monkey.examined for monkey in more_annoying], reverse=True)
	print("The most examinative monkeys product are:", examination_results_20[0]*examination_results_20[1])
	print("The most examinative of the more annoying monkeys product are:", examination_results_10k[0]*examination_results_10k[1])


if __name__ == '__main__':
	main()
