def main(test):
    rows = open("input_easy.txt").read().split("\n")
    if not test:
        rows = open("input.txt").read().split("\n")

    total = 0
    for sack in rows:
        # should contain a set long N of equal items
        copy = [item for item in sack[:int(len(sack) / 2)] if item in sack[int(len(sack) / 2):]][0]
        total += ord(copy) - ord('a') + 1 if copy.islower() else ord(copy) - ord('A') + 27
    print("The total priority is:", total)

    group_total = 0
    for i in range(int(len(rows)/3)):
        sets = []
        for elf in rows[i*3:i*3+3]:
            sets.append(set([letter for letter in elf]))
        common = sets[0].intersection(sets[1], sets[2]).pop()
        group_total += ord(common) - ord('a') + 1 if common.islower() else ord(common) - ord('A') + 27
    print("The total priority of each group is:", group_total)


if __name__ == '__main__':
    main(False)
