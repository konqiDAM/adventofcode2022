from string import ascii_lowercase

alphabet = ascii_lowercase
list_letters = alphabet + alphabet.upper()
lines: [str] = []


def read_file():
    with open('../Inputs/Day3.txt', 'r') as file:
        lines: list[str] = file.readlines()
    return lines


def count_value_part1():
    sumPostion = 0
    count = 0
    for line in lines:
        mid_position = int(len(line) / 2)
        set1 = set(line[:mid_position])
        set2 = set(line[mid_position:])
        common_chars = set1 & set2
        for char in common_chars:
            try:
                sumPostion += int(list_letters.index(char)) + 1
            except Exception:
                print()
    print(sumPostion)


def count_value_part2():
    sumPostion = 0
    count = 0
    for line in lines:
        #print(line)
        count += 1
        if count == 1:
            set1 = set(line)
        elif count == 2:
            set2 = set(line)
        else:
            set3 = set(line)
            #print("L1: " + str(set1) + "\n L2: " + str(set2) + "\n L3: " + str(set3))
            common_chars = set1 & set2 & set3
            for char in common_chars:
                #print(str(count) + ", " + str(common_chars))
                try:
                    sumPostion += int(list_letters.index(char)) + 1
                except Exception:
                    print(char)
            count = 0
    print(sumPostion)


if __name__ == '__main__':
    lines = read_file()
    count_value_part1()
    count_value_part2()
