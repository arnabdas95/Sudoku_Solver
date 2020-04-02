# ................................SUDOKU_SOLVER USING BOT...............................



# GLOBAL DECLEARATION
# DEFINE 2D GRID LIST FOR SUDOKU BOARD INITIALLY ALL ARE ZEROES
rows, cols = (9, 9)
sudoku_grid = [[0 for i in range(cols)] for j in range(rows)]




# ...............................FUNCTION DEFINITION..........................
# FUNCTION FOR GETTING THE UNSOLVED SUDOKU FROM USER
def get_unsolved_sudoku():
    print("Enter the unsolved sudoku use 0 for blank cell. ")
    for row in range(rows):
      for col in range(cols):
         sudoku_grid[row][col] = check_correct_ip()
         #sudoku_grid[row][col] = int(input("Enter digit :  "))






# FUNCTION FOR PRINTING GRID
def display_grid():
    for row in range(rows):
        if row % 3 == 0 and row != 0:
            print("-----------------------")

        for col in range(cols):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                   print(sudoku_grid[row][col])
            else:
                    print("{} ".format(sudoku_grid[row][col]), end="")






# FUNCTION FOR CHECKING EMPTY BLOCK
def find_empty_block(sudoku_grid, block):
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] == 0:
                block[0] = row
                block[1] = col
                return True
    return False






# FUNCTION FOR COMPARE THE NUMBER WITH ASSIGNED NUMBERS IN THE ROW WITH AND RETURNS BOOL
def find_row(sudoku_grid, row, num):
    for i in range(9):
        if sudoku_grid[row][i] == num:
            return True
    return False







# FUNCTION FOR COMPARE THE NUMBER WITH ASSIGNED NUMBERS IN THE COLUMN WITH AND RETURNS BOOL
def find_col(sudoku_grid, col, num):
    for i in range(9):
        if sudoku_grid[i][col] == num:
            return True
    return False






# FUNCTION FOR CHECKING 3*3 SUB BOXES
def find_sub_box(sudoku_grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if sudoku_grid[i + row][j + col] == num:
                return True
    return False





# FUNCTION FOR CHECKING A NUMBER CAN BE ASSIGNED OR NOT IN A BLOCK
def check_for_assign(sudoku_grid, row, col, num):
    return not find_row(sudoku_grid, row, num) and not find_col(sudoku_grid, col, num) and not find_sub_box(sudoku_grid,row - row % 3,col - col % 3, num)




# FUNCTION FOR SOLVE SUDOKU WITH BACKTRACKING
def solve(sudoku_grid):
    block = [0, 0]
    #base case for backtracking
    if not find_empty_block(sudoku_grid, block):
        return True
    row = block[0]
    col = block[1]

    for num in range(1, 10):
        if check_for_assign(sudoku_grid, row, col, num):
            sudoku_grid[row][col] = num
            if solve(sudoku_grid):
                return True
            sudoku_grid[row][col] = 0
    return False



#function for checking correct input
def check_correct_ip():
    while True:
        try:
            return int(input("Enter digit : "))
        except:
            print("woops!!enter only digit!")


# .......................MAIN DRIVER .............

get_unsolved_sudoku()
print("\nbefore solution:\n")
display_grid()

if solve(sudoku_grid):
    print("\nafter  solution:\n")
    display_grid()

else:
    print("No solution exists")
