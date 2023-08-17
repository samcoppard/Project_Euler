"""
What is the greatest product of four adjacent numbers in the same direction (up, down,
left, right, or diagonally) in the 20×20 grid below?

N.B. This solution and code is messy, but it does work.
"""

# Getting the grid into a usable structure is awkward enough -
# going for a list of 20 lists of 20 numbers each
a = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

# Split up the individual numbers
numbers = a.split(" ")


# Create a function to turn each row of numbers into a list, then add them to the grid,
# and keep going until all 400 numbers are in there
def twenty_at_a_time(start, end, grid=[]):
    # Create a list for each row of 20 numbers
    line_of_twenty = []
    for i in range(start, end):
        line_of_twenty.append(
            int(numbers[i])
        )  # Turn the number-strings back into actual numbers
    grid.append(line_of_twenty)

    start += 20
    end += 20

    if start < 400:
        twenty_at_a_time(start, end, grid)

    return grid


# Run the function to get the grid
original_grid = twenty_at_a_time(0, 20)


def find_max_row_product(grid, max_product):
    """Find the highest product of 4 consecutive numbers in any of the rows of a grid"""
    for row in grid:
        # Ignore rows with less than 4 numbers
        if len(row) < 4:
            continue
        else:
            product = row[0] * row[1] * row[2] * row[3]
        if product > max_product:
            max_product = product
        if len(row) > 4:
            for i in range(4, len(row)):
                if row[i - 4] == 0:
                    product = row[i - 3] * row[i - 2] * row[i - 1] * row[i]
                else:
                    product = (product / row[i - 4]) * row[i]
                if product > max_product:
                    max_product = product

    return int(max_product)


# Turn the columns into rows so that we can use the same formula again
column_rows_grid = []
for i in range(20):
    column_row = [original_grid[j][i] for j in range(20)]
    column_rows_grid.append(column_row)


# Create a new set of rows to make calculations easy for the first of four sets of diagonals
# (the top left diagonals)
rows_for_top_left_diag = []
for n in range(20):
    row = []
    i = n
    for j in range(n + 1):
        row.append(original_grid[i][j])
        i -= 1
        j += 1
    rows_for_top_left_diag.append(row)


# Now do the same for the top right diagonals, by reversing each row,
# and then repeating the process for the top left diagonals

top_right_grid = []
for ele in original_grid:
    reversed_list = [num for num in reversed(ele)]
    top_right_grid.append(reversed_list)

rows_for_top_right_diag = []
for n in range(20):
    row = []
    i = n
    for j in range(n + 1):
        row.append(top_right_grid[i][j])
        i -= 1
        j += 1
    rows_for_top_right_diag.append(row)


# Now do the same for the bottom left diagonals, by first reversing the order of the rows

bottom_left_grid = original_grid[::-1]

rows_for_bottom_left_diag = []
for n in range(20):
    row = []
    i = n
    for j in range(n + 1):
        row.append(bottom_left_grid[i][j])
        i -= 1
        j += 1
    rows_for_bottom_left_diag.append(row)


# Finally do the same for the bottom right diagonals

bottom_right_grid = []

for ele in bottom_left_grid:
    reversed_list = [num for num in reversed(ele)]
    bottom_right_grid.append(reversed_list)

rows_for_bottom_right_diag = []

for n in range(20):
    row = []
    i = n
    for j in range(n + 1):
        row.append(bottom_right_grid[i][j])
        i -= 1
        j += 1
    rows_for_bottom_right_diag.append(row)


# Find the maximum product across all of the rearranged grids
grids = [
    original_grid,
    column_rows_grid,
    rows_for_top_left_diag,
    rows_for_top_right_diag,
    rows_for_bottom_left_diag,
    rows_for_bottom_right_diag,
]

final_max_product = 0

for ele in grids:
    if find_max_row_product(ele, 0) > final_max_product:
        final_max_product = find_max_row_product(ele, 0)

print(final_max_product)
