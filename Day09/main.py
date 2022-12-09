# COSTANTS - useful mapping
direction_map = 'UDLR'
deltax = [0, 0, -1, 1]
deltay = [1, -1, 0, 0]


class Rope:
	def __init__(self):
		self.hx = 0
		self.hy = 0
		self.tx = 0
		self.ty = 0
		self.h_visited = [(0, 0)]
		self.t_visited = [(0, 0)]

	def visit_head(self):
		self.h_visited.append((self.hx, self.hy))

	def visit_tail(self):
		self.t_visited.append((self.tx, self.ty))

	def visited_tails(self):
		return len(set(self.t_visited))

	def move_head(self, direction):
		dir_value = direction_map.index(direction)
		self.hx += deltax[dir_value]
		self.hy += deltay[dir_value]
		self.visit_head()
		self.follow()

	def follow(self):
		dx = self.hx-self.tx
		dy = self.hy-self.ty
		if max(abs(dx), abs(dy)) > 1:
			# the rope must move
			self.tx += int(dx/abs(dx)) if dx != 0 else 0
			self.ty += int(dy/abs(dy)) if dy != 0 else 0
			self.visit_tail()


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	rope = Rope()
	for row in rows:
		direct, times = row.split(" ")
		times = int(times)

		while times:
			rope.move_head(direct)
			times -= 1

		# print(rope.hx, rope.hy, "-", rope.tx, rope.ty)
	print("The number of spaces visited by tail is:", rope.visited_tails())


if __name__ == '__main__':
	main(False)
