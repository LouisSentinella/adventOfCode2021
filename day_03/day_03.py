with open("input.txt", "r") as file:
    inputs_list = [[int(char) for char in line.strip()] for line in file]
file.close()


def col_count(input_list):
    return [sum(x) for x in zip(*input_list)]


def part_one(input_list):
    final_gamma = ''.join(['1' if x > 500 else '0' for x in col_count(input_list)])
    final_epsilon = ''.join(['1' if x == '0' else '0' for x in final_gamma])
    return (int(final_gamma, 2) * int(final_epsilon, 2))


def part_two(input_list):
    original_list = input_list
    for i in range(0, 12):
        col_total = col_count(input_list)
        if len(input_list) != 1:
            if col_total[i] > len(input_list) / 2:
                cleared_list = [x for x in input_list if x[i] == 1]
            elif col_total[i] < len(input_list) / 2:
                cleared_list = [x for x in input_list if x[i] == 0]
            else:
                cleared_list = [x for x in input_list if x[i] == 1]
            input_list = cleared_list
        else:
            break

    oxygen_rating = int(''.join([str(v) for v in input_list[0]]), 2)
    input_list = original_list
    for i in range(0, 12):
        col_total = col_count(input_list)
        if len(input_list) != 1:
            if col_total[i] > len(input_list) / 2:
                cleared_list = [x for x in input_list if x[i] == 0]
            elif col_total[i] < len(input_list) / 2:
                cleared_list = [x for x in input_list if x[i] == 1]
            else:
                cleared_list = [x for x in input_list if x[i] == 0]
            input_list = cleared_list
        else:
            break
    c02_scrubber_rating = int(''.join([str(v) for v in input_list[0]]), 2)
    return oxygen_rating * c02_scrubber_rating


print(part_one(inputs_list))
print(part_two(inputs_list))
