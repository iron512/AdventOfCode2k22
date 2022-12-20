def compute_v3(item_string):
	results = {}
	exec("res = " + item_string, {}, results)
	return results['res']


def compute(l1, l2):
	while l1:
		if not l2:
			return -1

		exam1 = l1.pop(0)
		exam2 = l2.pop(0)

		if type(exam1) is int and type(exam2) is int:
			if exam1 < exam2:
				return 1
			elif exam1 > exam2:
				return -1
		else:
			# One or both are lists
			if type(exam1) is int:
				exam1 = [exam1]
			if type(exam2) is int:
				exam2 = [exam2]
			result = compute(exam1, exam2)
			if result != 0:
				return result
	return 1 if len(l2) != 0 else 0


def main(test=False):
	rows = open("input_easy.txt").read().split("\n\n")
	rows = open("input_hard.txt").read().split("\n\n")
	if not test:
		rows = open("input.txt").read().split("\n\n")

	total = 0
	for idx, row in enumerate(rows):
		left, right = [compute_v3(item) for item in row.split("\n")]
		if compute(left, right) == 1:
			total += idx + 1

	print("The sum  of the correct pairs indexes is:", total)


if __name__ == '__main__':
	main()
