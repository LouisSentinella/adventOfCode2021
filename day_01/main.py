def part_one(input_list):
    return sum([1 for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]])


def part_two(input_list):
    return part_one([sum(input_list[n:n + 3]) for n in range(0, len(input_list))])


with open("input.txt", "r") as file:
    inputs_list = [int(line.strip()) for line in file]
file.close()

print(part_one(inputs_list))
print(part_two(inputs_list))
