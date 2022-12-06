import string
# As suggest by my brilliant colleague
MAP = "_" + string.ascii_lowercase + string.ascii_uppercase


def main(test):
    rows = open("input_easy.txt").read().split("\n")
    if not test:
        rows = open("input.txt").read().split("\n")

    total = 0
    for sack in rows:
        # should contain a set long N of equal items
        copy = set(sack[:int(len(sack) / 2)]).intersection(set(sack[int(len(sack) / 2):])).pop()
        total += MAP.index(copy)
    print("The total priority is:", total)

    group_total = 0
    for i in range(int(len(rows)/3)):
        sets = []
        for elf in rows[i*3:i*3+3]:
            sets.append(set([letter for letter in elf]))
        common = sets[0].intersection(sets[1], sets[2]).pop()
        group_total += MAP.index(common)
    print("The total priority of each group is:", group_total)


if __name__ == '__main__':
    main(False)
