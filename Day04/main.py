def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	overlap = 0
	overlap_partial = 0
	for pair in rows:
		elf1, elf2 = pair.split(",")
		elf1_s, elf1_e = [int(val) for val in elf1.split("-")]
		elf2_s, elf2_e = [int(val) for val in elf2.split("-")]
		elf1_range = set(range(elf1_s, elf1_e + 1))
		elf2_range = set(range(elf2_s, elf2_e + 1))

		intersect = elf1_range.intersection(elf2_range)

		if len(intersect) == min(len(elf1_range),len(elf2_range)):
			overlap += 1

		if (len(intersect)) != 0:
			overlap_partial += 1

	print("The overlapping sets are:", overlap)
	print("The partially overlapping sets are:", overlap_partial)


if __name__ == '__main__':
	main(False)
