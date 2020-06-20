# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

w, h = 21, 21
matrix = [[1 for x in range(w)] for y in range(h)]


def process_matrix():
    for i in range(1, w):
        for j in range(1, h):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


process_matrix()

print("Result: ", matrix[w-1][h-1])
