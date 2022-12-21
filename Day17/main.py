rocks = [
	["0011110"], 	# The straight horizontal line
	["0001000", "0011100", "0001000"],  # The cross
	["0011100", "0000100", "0000100"],  # The L shape (reversed, in order to be appended correctly)
	["0010000", "0010000", "0010000", "0010000"],  # The straight vertical line
	["0011000", "0011000"]  # the cube
]
corridor = ["2222222", "0000000", "0000000", "0000000"]


def show_map():
	for line in reversed(corridor):
		print(line.replace("0", ".").replace("1", "#").replace("2", "#"))
	print()


def move_left():
	stop = False
	for i in range(len(corridor)):
		for j in range(len(corridor[i])):
			if corridor[i][j] == '1':
				if j - 1 < 0 or corridor[i][j - 1] == '2':
					stop = True

	if not stop:
		for i in range(len(corridor)):
			for j in range(len(corridor[i])):
				if corridor[i][j] == '1':
					corridor[i] = corridor[i][:j-1] + "10" + corridor[i][j + 1:]
	return stop


def move_right():
	stop = False
	for i in range(len(corridor)):
		for j in range(len(corridor[i])):
			if corridor[i][j] == '1':
				if j+1 >= len(corridor[i]) or corridor[i][j+1] == '2':
					stop = True

	if not stop:
		for i in range(len(corridor)):
			for j in range(len(corridor[i])-1, -1, -1):
				if corridor[i][j] == '1':
					corridor[i] = corridor[i][:j] + "01" + corridor[i][j+2:]
	return stop


def move_down(direction):
	if direction == '<':
		move_left()
	elif direction == '>':
		move_right()

	stop = False
	for i in range(len(corridor)):
		for j in range(len(corridor[i])):
			if corridor[i][j] == '1':
				if corridor[i-1][j] == '2':
					stop = True

	if not stop:
		for i in range(len(corridor)):
			for j in range(len(corridor[i])):
				if corridor[i][j] == '1':
					corridor[i - 1] = corridor[i-1][:j] + corridor[i][j] + corridor[i-1][j + 1:]
					corridor[i] = corridor[i][:j] + '0' + corridor[i][j + 1:]
	return not stop


def settle(value):
	for i in range(len(corridor)):
		for j in range(len(corridor[i])):
			if corridor[i][j] == '1':
				corridor[i] = corridor[i][:j] + '2' + corridor[i][j + 1:]

	target = "0000000"
	while target in corridor:
		corridor.remove(target)

	corridor.extend([target, target, target])
	return value


def main(test=False):
	rows = [char for char in open("input_easy.txt").read()]
	if not test:
		rows = [char for char in open("input.txt").read()]

	count = 2022
	# count = 1000000000
	value = 0
	for i in range(count):
		# spawn rock
		rock = rocks[i % 5]
		corridor.extend(rock)

		fall = True
		while fall:
			direction = rows.pop(0)
			rows.append(direction)
			fall = move_down(direction)
		value = settle(value)
	# show_map()
	print("\nThe tower of rocks is high exactly", len(corridor)-4, "blocks")


if __name__ == '__main__':
	main(False)
