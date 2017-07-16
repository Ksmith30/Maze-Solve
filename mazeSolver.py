import os.path

# Open .txt file
def loadMaze(_filename):
    with open(_filename) as f:
        print("Maze: \n" + f.read())
        result = [[x for x in line.split()] for line in f]
    return result

# Checks to see if file input is valid
#filename = input("Input filename: ")
filename = "maze.txt"
if os.path.isfile(filename):
    maze = loadMaze(filename)
else:
    print("The file could not be opened.")

