def main(test):
    rows = open("input_easy.txt").read()
    if not test:
        rows = open("input.txt").read()

    elves = rows.split("\n\n")
    calories = []

    for elf in elves:
        values = elf.split("\n")
        calories.append(sum([int(val) for val in values]))

    calories.sort(reverse=True)

    print("The max calories elf is: ", calories[0])
    print("The group of elves is:", sum(calories[0:3]))


if __name__ == '__main__':
    main(False)
