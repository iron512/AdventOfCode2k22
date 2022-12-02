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
def match_eval_original(me, opp):
    if gesture_next(me) == opp:
        # lost
        return 0
    elif gesture_prec(me) == opp:
        # won
        return 6
    else:
        # draw
        return 3


def match_eval_predict(me, opp):
    if me == 1:
        # lost
        return gesture_prec(opp)
    elif me == 3:
        # won
        return gesture_next(opp)
    else:
        # draw
        return opp


def main(test):
    rows = open("input_easy.txt").read()
    if not test:
        rows = open("input.txt").read()

    matches = rows.split("\n")
    total_original = 0
    total_predict = 0
    for match in matches:
        # part 1
        elf, you = [hand_map(gesture) for gesture in match.split(" ")]
        total_original += you + match_eval_original(you, elf)
        # part 2
        total_predict += match_eval_predict(you, elf) + (you-1)*3

    print("Your total score against", len(matches), "elves is:", total_original)
    print("The score you should try to get against", len(matches), "elves is:", total_predict)


if __name__ == '__main__':
    main(False)
