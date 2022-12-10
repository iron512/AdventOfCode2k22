required = [20, 60, 100, 140, 180, 220]


def main(test=False):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	# cycle 0 doesn't exist.
	# Cycle 1 starts without any effect
	cycles = ['_', '_']
	screen = ['█']
	register_x = 1
	for row in rows:
		if row != 'noop':
			cycles.append(register_x)
			screen.append("█" if (len(cycles)-1) % 40 in range(cycles[-1], cycles[-1]+3) else " ")
			_, value = row.split(" ")
			register_x += int(value)

		cycles.append(register_x)
		screen.append("█" if (len(cycles)-1) % 40 in range(cycles[-1], cycles[-1] + 3) else " ")

	total = 0
	for cycle in required:
		total += cycle * cycles[cycle]
	print("The sum of the signal strength is:", total)

	print("The screen outputs: ")
	for i in range(6):
		print("".join(screen[i*40:i*40+40]))
		# For some unknown reason, the last character of each row doesn't makes sense with the others
		# And also with the puzzle input. The solution plots it almost perfectly (meaning that most of the code is
		# right. I really don't know why this strange behaviour


if __name__ == '__main__':
	main(False)
