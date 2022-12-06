def main(test):
	rows = open("input_easy.txt").read()
	if not test:
		rows = open("input.txt").read()

	for i in range(len(rows)):
		if len(set(rows[i:i+4])) == 4:
			print("The sequence marker ends at:", i+4)
			break

	for i in range(len(rows)):
		if len(set(rows[i:i+14])) == 14:
			print("The message marker ends at:", i+14)
			break


if __name__ == '__main__':
	main(True)
