def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	inclusions = 0
	overlap = 0
	for pair in rows:
		[elf1_start, elf1_end], [elf2_start, elf2_end] = [interval.split("-") for interval in pair.split(",")]
		elf1_range = set(range(int(elf1_start), int(elf1_end) + 1))
		elf2_range = set(range(int(elf2_start), int(elf2_end) + 1))

		intersect = elf1_range.intersection(elf2_range)

		if len(intersect) == min(len(elf1_range), len(elf2_range)):
			inclusions += 1

		if len(intersect) != 0:
			overlap += 1

	print("The overlapping sets are:", inclusions)
	print("The partially overlapping sets are:", overlap)


if __name__ == '__main__':
	main(False)
