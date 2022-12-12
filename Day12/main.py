import string
import networkx as nx

heatmap = 'S' + string.ascii_lowercase + "E"
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Tile:
	def __init__(self, matrix, value):
		self.matrix = matrix
		self.value = value
		self.visited = False


def main(test=False):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	random_prime = 11393
	graph = nx.DiGraph()

	starting_point = 0
	starting_points = []
	ending_point = -1
	for idx, row in enumerate(rows):
		for idy, char in enumerate(row):
			node_id = idx*random_prime + idy
			graph.add_node(node_id, height=heatmap.index(char))

			if char == 'S':
				starting_point = node_id

			if char == 'a':
				starting_points.append(node_id)

			if char == 'E':
				ending_point = node_id

	# fill the edges
	for idx, row in enumerate(rows):
		for idy, char in enumerate(row):
			node_id = idx*random_prime + idy
			node = graph.nodes[node_id]
			for dx, dy in directions:
				neighbour_id = (idx + dx)*random_prime + idy + dy
				if neighbour_id in graph.nodes:
					dest = graph.nodes[neighbour_id]
					if dest['height'] <= node['height'] + 1:
						graph.add_edge(node_id, neighbour_id)

	# Part 1
	shortest_from_s = len(nx.shortest_path(graph, starting_point, ending_point))-1
	print("The shortest path starting from S to E takes", shortest_from_s, "steps")

	# Part 2
	path_lengths = []
	for sp in starting_points:
		try:
			path_lengths.append(len(nx.shortest_path(graph, sp, ending_point))-1)
		except:
			pass
			# print("No path found. Skipping")

	print("The shortest path starting from any deep (a) point to E takes", min(path_lengths), "steps")


if __name__ == '__main__':
	main()
