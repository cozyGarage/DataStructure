class MaxProfitPathFinder:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.matrix = None
        self.max_profit_matrix = None
        self.path_matrix = None

    #Load input file to matrix  
    def load_matrix(self):
        try:
            with open(self.input_file, 'r') as file:
                self.matrix = [list(map(int, line.strip().split())) for line in file]
        except FileNotFoundError:
            print(f"Error: Input file '{self.input_file}' not found.")
            return False
        return True

    def compute_max_profit(self):
        if self.matrix is None:
            print("Error: Matrix not loaded. Call load_matrix() first.")
            return
        #Calculate the dimensions of the matrix
        n = len(self.matrix)
        m = len(self.matrix[0])

        # Create a matrix to store the maximum profit
        self.max_profit_matrix = [[0] * m for _ in range(n)]

        # Initialize the top-left cell of max_profit_matrix
        self.max_profit_matrix[0][0] = self.matrix[0][0]

        # Calculate the first row of max_profit_matrix
        for j in range(1, m):
            self.max_profit_matrix[0][j] = self.max_profit_matrix[0][j - 1] + (1 if self.matrix[0][j] == 1 else -1)

        # Calculate the first column of max_profit_matrix
        for i in range(1, n):
            self.max_profit_matrix[i][0] = self.max_profit_matrix[i - 1][0] + (1 if self.matrix[i][0] == 1 else -1)

        # Fill in the rest of max_profit_matrix
        for i in range(1, n):
            for j in range(1, m):
                self.max_profit_matrix[i][j] = max(self.max_profit_matrix[i - 1][j], self.max_profit_matrix[i][j - 1]) + (1 if self.matrix[i][j] == 1 else -1)

    def create_path_matrix(self):
        if self.max_profit_matrix is None:
            print("Error: Max profit matrix not computed. Call compute_max_profit() first.")
            return
        n = len(self.matrix)
        m = len(self.matrix[0])

        # Create a matrix to store the path
        self.path_matrix = [['-'] * m for _ in range(n)]
        i, j = n - 1, m - 1

        while i > 0 or j > 0:
            self.path_matrix[i][j] = '$'
            if i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            elif self.max_profit_matrix[i - 1][j] > self.max_profit_matrix[i][j - 1]:
                i -= 1
            else:
                j -= 1
        self.path_matrix[0][0] = '$'
        
    def write_output_file(self):
        if self.path_matrix is None:
            print("Error: Path matrix not created. Call create_path_matrix() first.")
            return
        with open(self.output_file, 'w') as file:
            file.write(f"Max Profit: {self.max_profit_matrix[-1][-1]}\n")
            for row in self.path_matrix:
                file.write(" ".join(row) + '\n')

    def process_matrix(self):
        if not self.load_matrix():
            return
        self.compute_max_profit()
        self.create_path_matrix()
        self.write_output_file()

# Example usage:
if __name__ == '__main__':
    input_file = 'bigtable.txt'
    output_file = 'results.txt'
    path_finder = MaxProfitPathFinder(input_file, output_file)
    path_finder.process_matrix()
