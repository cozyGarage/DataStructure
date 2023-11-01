# Read the binary matrix from Bigtable.txt
matrix = []
with open('Bigtable.txt', 'r') as file:
    for line in file:
        row = [int(x) for x in line.split()]
        matrix.append(row)

# Calculate the dimensions of the matrix
rows = len(matrix)
cols = len(matrix[0])

# Create a matrix to store the maximum profit for each cell
max_profit = [[0] * cols for _ in range(rows)]

# Create a matrix to store the path characters
path_matrix = [[''] * cols for _ in range(rows)]

# Initialize the first cell with the profit value and the path character
max_profit[0][0] = matrix[0][0]
path_matrix[0][0] = '*' if matrix[0][0] == 1 else '-'

# Fill in the first row and column
for i in range(1, rows):
    max_profit[i][0] = max_profit[i - 1][0] + (1 if matrix[i][0] == 1 else -1)
    path_matrix[i][0] = '*' if matrix[i][0] == 1 else '-'

for j in range(1, cols):
    max_profit[0][j] = max_profit[0][j - 1] + (1 if matrix[0][j] == 1 else -1)
    path_matrix[0][j] = '*' if matrix[0][j] == 1 else '-'

# Fill in the rest of the matrix
for i in range(1, rows):
    for j in range(1, cols):
        right_profit = max_profit[i][j - 1] + (1 if matrix[i][j] == 1 else -1)
        down_profit = max_profit[i - 1][j] + (1 if matrix[i][j] == 1 else -1)

        if right_profit >= down_profit:
            max_profit[i][j] = right_profit
            path_matrix[i][j] = '*' if matrix[i][j] == 1 else '-'
        else:
            max_profit[i][j] = down_profit
            path_matrix[i][j] = '*' if matrix[i][j] == 1 else '-'

# Print the maximum profit
print("Maximum Profit:", max_profit[rows - 1][cols - 1])

# Print the path with marked '*' for 1s and '-' for 0s
for row in path_matrix:
    print(''.join(row))


#Print the path with marked '*' for 1s and '-' for 0s
for row in max_profit:
    print(row)
    print('\n')

# # After you have computed the maximum profit and filled in the path_matrix:
# # Initialize the indices for backtracking
# i = rows - 1
# j = cols - 1

# # Keep track of the highlighted path
# highlighted_path_matrix = [[' '] * cols for _ in range(rows)]

# # Start from the bottom-right corner and backtrack to the top-left corner
# while i > 0 or j > 0:
#     # Mark the current cell in the highlighted path
#     highlighted_path_matrix[i][j] = '$'

#     # Move left if the best path was from the left
#     if j > 0 and max_profit[i][j - 1] >= max_profit[i - 1][j]:
#         j -= 1
#     # Move up if the best path was from the top
#     else:
#         i -= 1

# # Mark the starting cell in the highlighted path
# highlighted_path_matrix[0][0] = '*'

# # Print the highlighted path
# for row in highlighted_path_matrix:
#     print(''.join(row))



# Define the filename for the output path file
output_file = "PathWithMarks.txt"

# Open the file for writing
with open(output_file, "w") as output:
    # Write the path with marked '*' for 1s and '-' for 0s to the file
    for row in path_matrix:
        line = ''.join(row)
        output.write(line + '\n')

print("Path with marks saved to", output_file)
