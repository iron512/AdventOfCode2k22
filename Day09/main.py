# CONSTANTS - useful mapping
direction_map = 'UDLR'
deltax = [0, 0, -1, 1]
deltay = [1, -1, 0, 0]


class Knot:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.visited = []

	def move(self, direction):
		dir_value = direction_map.index(direction)
		self.x += deltax[dir_value]
		self.y += deltay[dir_value]
		self.visit()

	def follow(self, prior):
		dx = prior.x-self.x
		dy = prior.y-self.y
		if max(abs(dx), abs(dy)) > 1:
			# the rope must move
			self.x += int(dx/abs(dx)) if dx != 0 else 0
			self.y += int(dy/abs(dy)) if dy != 0 else 0
		self.visit()

	def visit(self):
		self.visited.append((self.x, self.y))


class Rope:
	def __init__(self, count):
		self.knots = [Knot() for i in range(count)]

	def visited_tails(self):
		return len(set(self.knots[-1].visited))

	def move(self, direction):
		prec = None
		for knot in self.knots:
			if prec is None:
				knot.move(direction)
			else:
				knot.follow(prec)
			prec = knot


def main(test):
	rows = open("input_easy.txt").read().split("\n")
	rows = open("input_hard.txt").read().split("\n")
	if not test:
		rows = open("input.txt").read().split("\n")

	ropefirst = Rope(2)
	ropesecond = Rope(10)
	for row in rows:
		direct, times = row.split(" ")
		times = int(times)

		while times:
			ropefirst.move(direct)
			ropesecond.move(direct)
			times -= 1

		# print(rope.hx, rope.hy, "-", rope.tx, rope.ty)
	print("The number of spaces visited by the 2 knot rope's tail is:", ropefirst.visited_tails())
	print("The number of spaces visited by the 10 knot rope's tail is:", ropesecond.visited_tails())


if __name__ == '__main__':
	main(False)
