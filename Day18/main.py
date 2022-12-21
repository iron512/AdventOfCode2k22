def main(test=False):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	# max value for my input is 21
	max_coord = 25
	size = range(max_coord)

	# map the matrix (in the beginning all 0, only air and no lava or water) and map the neighbours
	adj_matrix = [[[0 for _ in size] for _ in size] for _ in size]
	directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

	# fill the matrix with lava (represented by 1)
	for row in rows:
		x, y, z = [int(coord) for coord in row.split(",")]
		adj_matrix[x][y][z] = 1

	# Once the matrix is filled with lava, fill the water (represented by 2)
	# The water starts form (0, 0, 0) and it touches every neighbours
	queue = [(0, 0, 0)]
	while queue:
		x, y, z = queue.pop(0)
		if adj_matrix[x][y][z] == 0:
			adj_matrix[x][y][z] = 2

			for direction in directions:
				dx, dy, dz = direction
				if x + dx in size and y + dy in size and z + dz in size:
					queue.append((x+dx, y+dy, z+dz))

	faces = 0
	exposed_faces = 0
	# loop through all the blocks. Each lava block adds 6 faces
	# but if it touches another face (or the trapped air) it must be removed
	for x in size:
		for y in size:
			for z in size:
				if adj_matrix[x][y][z] == 1:
					faces += 6
					exposed_faces += 6

					for direction in directions:
						dx, dy, dz = direction
						if x+dx in size and y+dy in size and z+dz in size:
							faces -= 1 if adj_matrix[x+dx][y+dy][z+dz] == 1 else 0
							exposed_faces -= 1 if adj_matrix[x+dx][y+dy][z+dz] < 2 else 0

	print("The number of outside faces is:", faces)
	print("The number of exposed faces is:", exposed_faces)


if __name__ == '__main__':
	main(False)
