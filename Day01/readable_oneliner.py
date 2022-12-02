# Readable and 'actually making sense' oneliner
result = sorted([sum([int(val) for val in elf.split("\n")]) for elf in open("input.txt").read().split("\n\n")], reverse=True)
print("Part1:", result[0], "-- Part2:", sum(result[:3]))
