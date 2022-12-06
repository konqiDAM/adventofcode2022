lines = []

def read_file():
    with open('../Inputs/Day4.txt', 'r') as file:
        # Read all lines from the file
        lines: list[str] = file.readlines()
    return lines


def count_full_overlap():
    count = 0
    for line in lines:
        temp = line.split(",")
        temp2 = temp[0].split("-")
        value1 = int(temp2[0])
        value2 = int(temp2[1])
        temp2 = temp[1].split("-")
        value3 = int(temp2[0])
        value4 = int(temp2[1].strip())

        if value3 >= value1 and value2 >= value4:
            count += 1
        elif value1 >= value3 and value4 >= value2:
            count += 1
    print(count)


def count_partitial_overlap():
    count = 0
    for line in lines:
        temp = line.split(",")
        temp2 = temp[0].split("-")
        value1 = int(temp2[0])
        value2 = int(temp2[1])
        temp2 = temp[1].split("-")
        value3 = int(temp2[0])
        value4 = int(temp2[1].strip())

        if value4 >= value1 >= value3:
            count += 1
        elif value4 >= value2 >= value3:
            count += 1
        elif value1 <= value3 <= value2:
            count += 1
        elif value2 >= value4 >= value1:
            count += 1

    print(count)


if __name__ == '__main__':
    lines = read_file()
    count_full_overlap()
    count_partitial_overlap()