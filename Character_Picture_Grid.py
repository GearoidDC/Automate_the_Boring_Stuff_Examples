grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def gridprinter(grid):
    #Makes a for loop that runs for the sub list inside grid
    for i in range(len(grid[0])):
        #This for loop prints the element inside row without adding a newline
        for row in grid:
            print(row[i],end ="")
        #Adds a new line at end of each loop
        print()

test = gridprinter(grid)
