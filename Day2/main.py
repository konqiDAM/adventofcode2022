rock = "A"
paper = "B"
scissors = "C"
play_rock = "X"
play_paper = "Y"
play_scissors = "Z"
punctuation_rock = 1
punctuation_paper = 2
punctuation_scissors = 3
punctuation_lose = 0
punctuation_draw = 3
punctuation_win = 6
needs_lose = "X"
needs_draw = "Y"
needs_win = "Z"
punctuation_map = {
    play_rock: punctuation_rock,
    play_paper: punctuation_paper,
    play_scissors: punctuation_scissors,
}
punctuation_map_enemy = {
    rock: punctuation_rock,
    paper: punctuation_paper,
    scissors: punctuation_scissors,
}
equivalent_map = {
    play_rock: rock,
    play_paper: paper,
    play_scissors: scissors,
}
win_map = {
    scissors: rock,
    rock: paper,
    paper: scissors,
}
lose_map = {
    scissors: paper,
    rock: scissors,
    paper: rock,
}


def read_file():
    with open('../Inputs/Day2.txt', 'r') as file:
        # Read all lines from the file
        lines: list[str] = file.readlines()
    return lines


def print_input(lines):
    # Loop through the lines
    for line in lines:
        # Print each line
        print(line)


def calculate_score(lines):
    sumPoints = 0
    for line in lines:
        inter = calculate_outcome_points_part1(line[0], line[2])
        sumPoints += inter
    print(sumPoints)
    sumPoints = 0
    for line in lines:
        inter = calculate_outcome_points_part2(line[0], line[2])
        sumPoints += inter
    print(sumPoints)


def calculate_outcome_points_part1(enemy, me):
    # print("ENEMY: " +  enemy + ", me: " + me)
    extra_point = punctuation_map[me]
    #print("Extra poing is: " + str(extra_point))
    if equivalent_map[me] == enemy:
        #print("DRAW")
        return punctuation_draw + extra_point
    elif (enemy == rock and me == play_paper) or (enemy == paper and me == play_scissors) or (
            enemy == scissors and me == play_rock):
        #print("WIN")
        return punctuation_win + extra_point
    else:
        #print("LOSE")
        return punctuation_lose + extra_point


def calculate_outcome_points_part2(enemy, action):
    if action == needs_draw:
        return punctuation_draw + int(punctuation_map_enemy[enemy])
    elif action == needs_win:
        return punctuation_win + punctuation_map_enemy[win_map[enemy]]
    else:
        return punctuation_lose + punctuation_map_enemy[lose_map[enemy]]


if __name__ == '__main__':
    lines = read_file()
    # print_input(lines)
    calculate_score(lines)
