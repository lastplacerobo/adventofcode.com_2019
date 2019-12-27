import os
import numpy

# Returns the directory in which the code file is stored
# Returns the absolute path, but does NOT resolve symlinks in its argument
#os.path.dirname(os.path.abspath( __file__ ))

# Returns the directory in which the code file is stored
# Will first resolve any symbolic links in the path, and then return the absolute path.
#os.path.dirname(os.path.realpath(__file__))

# Returns the directory in which the code file is stored
#os.path.dirname(__file__)

# Returns the full path to the code file
#__file__

# Defaults to $PWD in your env. It's not where the script is located but where you were when you executed the script.
#os.getcwd()

############################

def main():

    dir = os.path.dirname(__file__)
    # open and join the dir with the file input as f
    with open(os.path.join(dir, "input")) as f:

        # Read from f, strip spaces, split into list by ","
        # Map takes function str (could also be int) and reads whole list and converts to str as a iterator
        # List converts the argument into a list and stores str in mem
        # mem = list(map(str, f.read().strip().split(',')))

        # List comprehension iterating trough lines and split on comma, saving in two lists
        wire_path1,wire_path2 = [i.split(',') for i in f.readlines()]

        # Clean up newline in last element
        wire_path1[-1] = wire_path1[-1].strip()
        wire_path2[-1] = wire_path2[-1].strip()

        grid_run(wire_path1)

        #print("\n")
        #print(grid_run(wire_path2))


def grid_run(route):

    # Dictionary for the final route_path
    route_path = {}

    # Variables for
    x_axis, y_axis, count = 0, 0, 0

    # With numpy create 2D array
    grid1 = numpy.zeros((10000, 10000))
    grid2 = numpy.zeros((10000, 10000))

    # Movement in the X and Y axis
    movement = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }

    # Iterate trough each route element, ie "R990" and onwards, so we work us trough the whole route from wire_path
    for element in route:

        # Iterate trough the specific routes each step in the grid, from zero to end, for R990 becomes 0-989.
        # By making an int of the element(R990), from 1 to end (string slicing). So R990 becomes "990" int by starting
        # after the letter in the element.
        # Taking the int and making a range of it, iterate trough this range
        for i in range((int(element[1:]))):

            # In this loop, we will track the steps for this specific route element
            #

            offset = movement[element[0]]
            x_axis += offset[0]
            y_axis += offset[1]
            count += 1

            route_path[(x_axis, y_axis)] = count

    return route_path


if __name__ == "__main__":
    main()