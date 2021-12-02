with open("input.txt", "r") as file:
    inputs_list = [line.strip() for line in file]
file.close()


def part_one(inputs_list):
    horizontal_final = 0
    vertical_final = 0
    for i in inputs_list:
        if i.startswith("forward"):
            horizontal_final += int(i.split()[1])
        elif i.startswith("up"):
            vertical_final -= int(i.split()[1])
        elif i.startswith("down"):
            vertical_final += int(i.split()[1])
    return horizontal_final * vertical_final


def part_two(inputs_list):
    horizontal_final = 0
    vertical_final = 0
    aim = 0
    for i in inputs_list:
        if i.startswith("forward"):
            horizontal_final += int(i.split()[1])
            vertical_final += (int(i.split()[1]) * aim)
        elif i.startswith("up"):
            aim -= int(i.split()[1])
        elif i.startswith("down"):
            aim += int(i.split()[1])
    return horizontal_final * vertical_final


print(part_one(inputs_list))
print(part_two(inputs_list))
