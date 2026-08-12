class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Transpose the board so columns become rows
        transposed_board = list(map(list, zip(*board)))

        # Create the 9 3x3 squares
        sudoku_square_list = []

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                square = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        square.append(board[row][col])

                sudoku_square_list.append(square)

        # Check rows, columns, and 3x3 squares
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            col = [x for x in transposed_board[i] if x != "."]
            square = [x for x in sudoku_square_list[i] if x != "."]

            if len(row) != len(set(row)):
                return False

            if len(col) != len(set(col)):
                return False

            if len(square) != len(set(square)):
                return False

        return True