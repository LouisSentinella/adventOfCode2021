class bingo_grid():

    def __init__(self, array):
        self.rows = array
        self.selected_numbers = [0 for _ in range(0, 25)]

    def is_bingo(self):
        for i in range(0, 5):
            x = self.selected_numbers[(5 * i):((5 * i) + 5)]
            if sum(x) == 5:
                return True
        for i in range(0, 5):
            x = self.selected_numbers[i::5]
            if sum(x) == 5:
                return True
        return False

    def unselected_numbers(self):
        unselected_numbers = []
        for index, val in enumerate(self.selected_numbers):
            if val == 0:
                unselected_numbers.append(self.rows[index])
        return unselected_numbers

    def select_number(self, num):
        for index, val in enumerate(self.rows):
            if val == num:
                self.selected_numbers[index] = 1


def part_one(grids, numbers):
    for number in numbers:
        for grid in grids:
            grid.select_number(number)
            if grid.is_bingo():
                return sum(grid.unselected_numbers()) * number


def part_two(grids, numbers):
    for number in numbers:
        for grid in grids:
            grid.select_number(number)
            if grid.is_bingo():
                grids.remove(grid)
                if len(grids) == 1:
                    return sum(grid.unselected_numbers()) * number


with open("input.txt", "r") as file:
    numbers_in_order = [int(x) for x in file.readline().strip().split(",")]
    file.readline()
    acc = 0
    bingo_grids = []
    current_grid = []
    for line in file:
        acc += 1
        if acc == 6:
            acc = 0
            bingo_grids.append(bingo_grid(current_grid))
            current_grid = []
        else:
            current_grid.extend([int(x) for x in line.strip().split()])
    bingo_grids.append(bingo_grid(current_grid))
file.close()

print(part_one(bingo_grids, numbers_in_order))
print(part_two(bingo_grids, numbers_in_order))
