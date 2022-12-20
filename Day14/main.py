import copy


def print_matrix(matrix):
	for line in matrix:
		print("".join(line[300:]))


def fall(matrix):
	x, y = 500, 0
	if matrix[y][x] == 'o':
		return True

	matrix[y][x] = 'o'

	while True:
		go_next = False
		for direction in [(0, 1), (-1, 1), (1, 1)]:
			if not go_next:
				dx, dy = direction
				if x+dx < len(matrix[0]) and y+dy < len(matrix):
					if matrix[y+dy][x+dx] == '.':
						matrix[y][x] = '.'
						y += dy
						x += dx
						matrix[y][x] = 'o'
						go_next = True
				else:
					return True
		if not go_next:
			return False


def main(test=False):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	max_x = -1
	max_y = -1

	walls = []
	for row in rows:
		wall = [tuple([int(coord) for coord in item.strip().split(",")]) for item in row.split("->")]
		walls.append(wall)
		for coord in wall:
			x, y = coord
			max_x = max(x, max_x)
			max_y = max(y, max_y)

	print(max_x, max_y)
	matrix = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

	for wall in walls:
		start = wall.pop(0)
		for coord in wall:
			start_x, start_y = start
			end_x, end_y = coord

			for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
				for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
					matrix[y][x] = '#'

			start = coord

	# Part1
	# print_matrix(matrix)

	# Part 2
	matrix_bottom = copy.deepcopy(matrix)

	engorge = 200
	for row in matrix_bottom:
		row.extend(['.' for _ in range(engorge)])
	matrix_bottom.append(['.' for _ in range(max_x + 1 + engorge)])
	matrix_bottom.append(['#' for _ in range(max_x + 1 + engorge)])
	# print_matrix(matrix_bottom)

	# CODE
	stopped = False
	stopped_bottom = False
	count = 0
	count_bottom = 0
	while not stopped_bottom:
		stopped_bottom = fall(matrix_bottom)
		count_bottom += 1

		if not stopped:
			stopped = fall(matrix)
			count += 1

	print_matrix(matrix)
	print()
	print_matrix(matrix_bottom)

	# remember to remove the last grain (which actually did not spawn)
	print("The total amount of fallen grains of sand is:", count-1)
	print("The total amount of fallen grains of sand in the bottom pit is:", count_bottom-1)


if __name__ == '__main__':
	main(False)
