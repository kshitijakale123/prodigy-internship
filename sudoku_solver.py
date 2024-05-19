def print_grid(grid):
    """Prints the Sudoku grid in a formatted way."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_safe(grid, row, col, num):
    """Checks if placing a number in the specified cell is valid."""
    # Check if the number is not in the current row, column, and 3x3 subgrid
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    empty_cell = find_empty_location(grid)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack

    return False

def find_empty_location(grid):
    """Finds an empty cell in the Sudoku grid."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku puzzle:")
    print_grid(grid)
    
    if solve_sudoku(grid):
        print("\nSolved Sudoku puzzle:")
        print_grid(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
