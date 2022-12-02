# Unreadable and unnecessarily complicated TRUE oneliner
[print("Part", int(i / 3)+1, ": ", sum(sorted([sum([int(kcal) for kcal in elf.split("\n")]) for elf in open("input.txt").read().split("\n\n")], reverse=True)[0:i]), sep="", end=" -- " if i == 1 else "\n") for i in [1, 3]]
