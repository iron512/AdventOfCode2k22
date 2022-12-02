def hand_map(value):
    if value == 'A' or value == 'X':
        return 1  # rock
    if value == 'B' or value == 'Y':
        return 2  # paper
    if value == 'C' or value == 'Z':
        return 3  # scissors


def gesture_next(val):
    if val == 3:
        return 1
    else:
        return val + 1


def gesture_prec(val):
    if val == 1:
        return 3
    else:
        return val - 1


# evaluates the match and the scores
def match_eval(me, opp):
    if gesture_next(me) == opp:
        # lost
        return 0
    elif gesture_prec(me) == opp:
        # won
        return 6
    else:
        # draw
        return 3


def main(test):
    rows = open("input_easy.txt").read()
    if not test:
        rows = open("input.txt").read()

    matches = rows.split("\n")
    total = 0
    for match in matches:
        elf, you = [hand_map(gesture) for gesture in match.split(" ")]
        total += you + match_eval(you, elf)

    print("Your total score against", len(matches), "elves is:", total)


if __name__ == '__main__':
    main(False)
