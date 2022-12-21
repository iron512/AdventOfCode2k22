def circular(pos, len):
	if pos == 0:
		return len
	if pos == len:
		return 0
	return pos % len


def main(test=False):
	rows = [int(val) for val in open("input_easy.txt").read().split("\n")]
	if not test:
		rows = [int(val) for val in open("input.txt").read().split("\n")]

	indexes = [i for i in range(len(rows))]
	for i in range(len(rows)):
		pos = indexes.index(i)

		element = rows.pop(pos)
		rows.insert(circular(pos+element, len(rows)), element)

		idx = indexes.pop(pos)
		indexes.insert(circular(pos+element, len(indexes)), idx)

	markers = [1000, 2000, 3000]
	starting_point = rows.index(0)
	tot = sum([rows[(starting_point+marker) % len(rows)] for marker in markers])
	print("The total sum of the three markers is:", tot)


if __name__ == '__main__':
	main(False)
