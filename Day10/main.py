required = [20, 60, 100, 140, 180, 220]


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	# cycle 0 doesn't exist.
	# Cycle 1 starts without any effect
	cycles = ['_', '_']
	register_x = 1
	for row in rows:
		if row == 'noop':
			cycles.append(register_x)

		else:
			cycles.append(register_x)
			_, value = row.split(" ")
			register_x += int(value)
			cycles.append(register_x)


	total = 0
	for cycle in required:
		total += cycle * cycles[cycle]
	print("The sum of the signal strength is:", total)


if __name__ == '__main__':
	main(False)
