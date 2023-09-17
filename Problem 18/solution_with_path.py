"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

N.B. I've added code to record the path taken as well.
"""

import time

start_time = time.time()

# Split the triangle into a list for each row
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split(
    "\n"
)

# Split each row into a list of numbers (still strings at this stage)
str_rows = [ele.split(" ") for ele in triangle]

# Turn each (string) number into an integer
int_rows = [[int(ele) for ele in row] for row in str_rows]

"""
We want to avoid checking every possible route here, so the basic approach is this:
Going row by row, starting at the top, find the highest total that can be reached by the
time you get to each number, and replace the original number in the triangle with this
running tally.
Calculate this running tally by adding the highest cumulative total of an adjacent number
in the previous row to each original number.
This cascades down the whole triangle, until you're left with the highest possible total
to reach each number on the bottom row. Just take the max of those, and we're done!
"""

# Create an empty list to store the path taken to get to each value
paths = []
paths.append([0])

# Loop over each row in the triangle (except the top row)
for i in range(1, len(int_rows)):
    row_paths = []

    # Add the first number of the previous row to the first number of the current row
    int_rows[i][0] += int_rows[i - 1][0]
    row_paths.append(f"{paths[i-1][0]}, 0")

    # Add the highest adjacent number of the previous row to each number of the current row
    for j in range(1, len(int_rows[i]) - 1):
        a = int_rows[i - 1][j - 1]
        b = int_rows[i - 1][j]
        c = max(a, b)
        int_rows[i][j] += c
        if c == a:
            row_paths.append(f"{paths[i-1][j-1]}, {j}")
        else:
            row_paths.append(f"{paths[i-1][j]}, {j}")
    
    # Add the last number of the previous row to the last number of the current row
    int_rows[i][-1] += int_rows[i - 1][-1]
    row_paths.append(f"{paths[i-1][-1]}, {len(int_rows[i]) - 1}")

    paths.append(row_paths)

# Find the highest value in the bottom row
max_total = max(int_rows[-1])

print(f"The highest possible total is {max_total}")

print(f"The highest totalling path is this: {paths[-1][9]}")

end_time = time.time()

print(f"This code took {(end_time - start_time):.6f}s to run")