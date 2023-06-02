import sys


class NQueensSolver:
    """NQueensSolver class that solves the n-queens problem"""

    def __init__(self, N):
        """initialize the NQueensSolver class"""
        self.n = N
        self.board = [[0 for col in range(N)] for row in range(N)]
        self.solutions = []

    def solve(self):
        """solve the n-queens problem and return the solutions"""
        self.place_queen(0)
        return self.solutions

    def place_queen(self, col):
        """place the queens on the board"""
        if col == self.n:
            self.solutions.append(self.get_queens())
            return True
        # for each row in the column
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.place_queen(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        """check if the queen is safe to place in the given
        position"""
        for c in range(col):
            if self.board[row][c] == 1:
                return False
        # check upper diagonal
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False
        # check lower diagonal
        for r, c in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False

        return True

    def get_queens(self):
        """get the queens on the board"""
        queens = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 1:
                    queens.append([row, col])
        return queens

    # def print_board(self):
    #     """print the board"""
    #     for row in self.board:
    #         print(row)


def main():
    """main function dealing with the constraints"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens = NQueensSolver(n)
    solutions = n_queens.solve()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """call main function"""
    main()
