import os.path
from sys import exit
from copy import deepcopy

WALL = "*"
SPACE = "_"
PATH = "!"


# Open .txt file
def load_maze(_filename):
    with open(_filename) as f:
        maze = [line.split() for line in f]
        print("Maze:\n" + f.read())
    return maze

# Check if valid move in maze


def valid_move(row, col, maze, seen):
    return row > len(maze) and row >= 0 and col > len(maze[0]) and col >= 0 and not seen[row][col] \
           and maze[row][col] != WALL

# See if entry point
def entryPoint(row, col, _maze):
    return (row == 0 or col == 0 or row == len(_maze - 1) or col == len(_maze[row]) - 1) and _maze[row][col] != WALL


# Checks to see if it can find Entry Point
def find_entrypoint(maze, startRow, startCol):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if entryPoint(i, j, maze):
                startRow = i
                startCol = j
                return {'startRow': startRow, 'startCol': startCol}
    return None

def check_direction(maze, start_row, start_col, r, c, seen, solution, direction):
    if direction is "N":
        r -= 1
    elif direction is "E":
        c += 1
    elif direction is "S":
        r += 1
    elif direction is "W":
        c -= 1

    if valid_move(r, c, maze, seen) and solve_helper(maze, start_row, start_col, r, c, seen, solution):
        solution[r][c] = PATH
        return {'maze': maze, 'seen': seen, 'solution': solution}



# Recursive helper function that helps to initialize the process
def solve_helper(maze, start_row, start_col, r, c, seen, solution):
    # Base case
    if entryPoint(r, c, maze) and (r != start_row or c != start_col):
        solution[r][c] = PATH
        return {'maze': maze, 'seen': seen, 'solution': solution}

    # Recursive Case
    seen[r][c] = True

    # North Case
    check_direction(maze, start_row, start_col, r, c, seen, solution, "N")

    # East Case
    check_direction(maze, start_row, start_col, r, c, seen, solution, "E")

    # South Case
    check_direction(maze, start_row, start_col, r, c, seen, solution, "S")

    # West Case
    check_direction(maze, start_row, start_col, r, c, seen, solution, "W")



# Begins the recursive process of solving
def solve(**arrays):
    # Make list of seen spaces in the maze
    arrays['seen'] = [[0] * (len(maze) - 1)]

    # See if there is an entry point
    start = find_entrypoint(maze, startRow=-1, startCol=-1)
    if not start:
        return False

    # Copy into solution
    solution = deepcopy(maze)

    # Use solveHelper to start recursive process
    dict = solve_helper(maze, start['startRow'], start['startCol'], start['startRow'], start['startCol'], seen,
                            solution)
    if solution is not None:
        return arrays['solution']
    else:
        return None


# Checks to see if file input is valid
# filename = input("Input filename: ")
filename = "maze.txt"
maze = []
seen = []
solution = []
arrays = {'maze': maze , 'seen' : seen, 'solution': solution}
if os.path.isfile(filename):
    arrays['maze'] = load_maze(filename)
else:
    print("The file could not be opened.")
    exit(0)
solution = solve(**arrays)
if solution is not None:
    print('Solution:\n' + solution)
else:
    print('No Solution')
