class Node:
	def __init__(self, parent, name, filetype, size, level):
		self.parent = parent
		self.name = name
		self.size = size
		self.filetype = filetype
		self.level = level
		self.children = []


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	lvl = 0
	max_lvl = 0

	home_folder = Node('', '/', 'dir', 0, lvl)
	current_folder = None

	directories = [home_folder]

	for row in rows:
		if row.startswith("$ cd "):
			folder_name = row.replace("$ cd ", "")

			if folder_name == '/':
				current_folder = home_folder
				lvl = 1
			elif folder_name == '..':
				current_folder = current_folder.parent
				lvl -= 1
			else:
				current_folder = [child for child in current_folder.children if child.name == folder_name][0]
				lvl += 1

		elif row.startswith("$ ls"):
			pass
		else:
			# just a file
			size, name = row.split(" ")
			if size == 'dir':
				node = Node(current_folder, name, 'dir', 0, lvl)
				current_folder.children.append(node)
				directories.append(node)
			else:
				current_folder.children.append(Node(current_folder, name, 'file', int(size), lvl))
		max_lvl = max(lvl, max_lvl)

	for outer in range(max_lvl, -1, -1):
		for directory in [directory for directory in directories if directory.level == outer]:
			directory.size = sum([element.size for element in directory.children])

	# print([(folder.name, folder.size) for folder in directories])
	smaller_sum = sum([folder.size for folder in directories if folder.size < 100000])
	print("The sum of the smaller (<100000) folders is: ", smaller_sum)


if __name__ == '__main__':
	main(False)
