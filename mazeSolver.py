import os.path
from sys import exit
from copy import deepcopy


WALL = "*"
SPACE = "_"
PATH = "!"


def load_maze(_filename):
    with open(_filename) as f:
        maze = [line.split() for line in f]
    return maze


def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))


def valid_move(row, col, maze, seen):
    return row < len(maze) and row >= 0 and col < len(maze[row]) and col >= 0 and not seen[row][col]\
           and maze[row][col] != WALL


def entry_point(row, col, maze):
    return (row == 0 or col == 0 or row == (len(maze) - 1) or col == (len(maze[row]) - 1)) and maze[row][col] != WALL


def find_entrypoint(maze, start_row, start_col):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if entry_point(i, j, maze):
                start_row = i
                start_col = j
    return start_row, start_col


def solve_helper(maze, start_row, start_col, r, c, seen, solution):
    if entry_point(r, c, maze) and (r != start_row or c != start_col):
        solution[r][c] = PATH
        return solution

    seen[r][c] = True

    if valid_move(r - 1, c, maze, seen) and solve_helper(maze, start_row, start_col, r - 1, c, seen, solution):
        solution[r][c] = PATH
        return solution
    elif valid_move(r, c + 1, maze, seen) and solve_helper(maze, start_row, start_col, r, c + 1, seen, solution):
        solution[r][c] = PATH
        return solution
    elif valid_move(r + 1, c, maze, seen) and solve_helper(maze, start_row, start_col, r + 1, c, seen, solution):
        solution[r][c] = PATH
        return solution
    elif valid_move(r, c - 1, maze, seen) and solve_helper(maze, start_row, start_col, r, c - 1, seen, solution):
        solution[r][c] = PATH
        return solution
    else:
        return False


def solve(maze):
    seen = [[False] * len(maze[0]) for _ in range(len(maze))]
    start_row, start_col = find_entrypoint(maze, -1, -1)
    if start_row is -1 or start_col is -1:
        return False

    solution = deepcopy(maze)
    return solve_helper(maze, start_row, start_col, start_row, start_col, seen, solution)


# filename = input("Input filename: ")
filename = "maze.txt"
if os.path.isfile(filename):
    init_maze = load_maze(filename)
    print("Maze:")
    print_maze(init_maze)
else:
    print("The file could not be opened.")
    exit(0)
print("Solution: ")

maze_solution = solve(init_maze)
if maze_solution:
    print_maze(maze_solution)
else:
    print("No solution.")




