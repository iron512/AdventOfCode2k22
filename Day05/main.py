import copy


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	reverse_stack = []
	instructions = []
	splitter = False
	for row in rows:
		if row.startswith(" 1"):
			splitter = True
			cargo_tot_lines = max([int(element) for element in row.split(" ") if element != ""])
		elif not splitter:
			reverse_stack.append(row)
		elif row != '':
			instructions.append(row)

	lines = []
	while reverse_stack:
		line = [container for idx, container in enumerate(reverse_stack.pop()) if (idx-1) % 4 == 0]
		while len(line) != cargo_tot_lines:
			line.append(" ")
		lines.append(line)

	stacks9000 = [[] for stack in range(cargo_tot_lines)]
	for line in lines:
		for column in range(cargo_tot_lines):
			if line[column] != " ":
				stacks9000[column].append(line[column])

	# SHIP PARSING END -- maronn' che dur
	stacks9001 = copy.deepcopy(stacks9000)

	for op in instructions:
		move, src, dst = [int(rule) for rule in op.replace("move", "").replace("from", "").replace("to", "").split(" ") if rule != ""]
		buffer = []

		while move:
			stacks9000[dst-1].append(stacks9000[src-1].pop())
			buffer.append(stacks9001[src-1].pop())
			move -= 1

		while buffer:
			stacks9001[dst-1].append(buffer.pop())

	print("The final top containers moved by CrateMover9000 are:", "".join([stack[-1] for stack in stacks9000]))
	print("The final top containers moved by CrateMover9001 are:", "".join([stack[-1] for stack in stacks9001]))


if __name__ == '__main__':
	main(False)
