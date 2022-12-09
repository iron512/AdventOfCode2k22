def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	matrix = []
	for row in rows:
		matrix.append([int(char) for char in row])

	invisible = 0
	line_of_sight = []
	for i in range(1, len(matrix)-1):
		for j in range(1, len(matrix[0])-1):
			# Here the magic happens
			col = [row[j] for row in matrix]
			directions = [matrix[i][:j][::-1], matrix[i][j+1:], col[:i][::-1], col[i+1:]]
			cardinals = [max(arr) for arr in directions]
			# print(directions) # Uncomment this line to help understand better the meaning of directions
			if matrix[i][j] <= min(cardinals):
				invisible += 1

			total = 1
			for direction in directions:
				count = 0
				obstruction = False
				for tree in direction:
					if not obstruction:
						count += 1
					if tree >= matrix[i][j]:
						obstruction = True
				total *= count
			line_of_sight.append(total)

	print("The number of visible trees is:", (len(matrix)*len(matrix[0])-invisible))
	print("The place where you can see most trees is:", max(line_of_sight))


if __name__ == '__main__':
	main(False)
