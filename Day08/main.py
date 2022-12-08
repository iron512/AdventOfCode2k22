def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	matrix = []
	for row in rows:
		matrix.append([int(char) for char in row])

	invisible = 0
	for i in range(1, len(matrix)-1):
		for j in range(1, len(matrix[0])-1):
			# Here the magic happens
			cardinals = [max(arr) for arr in [matrix[i][:j], matrix[i][j+1:], [row[j] for row in matrix][:i], [row[j] for row in matrix][i+1:]]]

			if matrix[i][j] <= min(cardinals):
				invisible += 1

	print("The number of visible trees is:", (len(matrix)*len(matrix[0])-invisible))


if __name__ == '__main__':
	main(True)
