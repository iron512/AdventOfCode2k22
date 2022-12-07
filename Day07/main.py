class Node:
	def __init__(self, parent, name, filetype, size, level):
		self.parent = parent
		self.name = name
		self.size = size
		self.filetype = filetype
		self.level = level
		self.children = []

	def print_directory_wrapper(self, max_levels):
		view_lvl = [True for lvl in range(max_levels+1)]
		self.print_directory(view_levels=view_lvl, last=True)

	def print_directory(self, view_levels, last):
		for i in range(self.level):
			if view_levels[i]:
				print("  │", end="")
			else:
				print("   ", end="")

		if last:
			print("  └─ ", end="")
			view_levels[self.level] = False
		else:
			print("  ├─ ", end="")
			view_levels[self.level] = True

		print(self.name, " (", round(self.size/1000), " KB)", sep="")
		for idx, child in enumerate(self.children):
			child.print_directory(view_levels, last=(idx == len(self.children)-1))


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	lvl = 0
	max_lvl = 0

	home_folder = Node('', '/', 'dir', 0, lvl)
	current_folder = None

	directories = [home_folder]
	# Input Parsing
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

	# Compute the folders
	for outer in range(max_lvl, -1, -1):
		for directory in [directory for directory in directories if directory.level == outer]:
			directory.size = sum([element.size for element in directory.children])

	# Part 1
	smaller_sum = sum([folder.size for folder in directories if folder.size < 100000])
	print("The sum of the smaller (<100000) folders is:", smaller_sum)

	# Part 2
	fs_required = home_folder.size - 40000000
	smaller_required = min([folder.size for folder in directories if folder.size > fs_required])
	print("The smaller directory large enough to fit the update is:", smaller_required)

	# Visualizer
	print("\nVisual structure:")
	home_folder.print_directory_wrapper(max_lvl)


if __name__ == '__main__':
	main(False)
