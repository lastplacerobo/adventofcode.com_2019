import os


# Returns the directory in which the code file is stored
# Returns the absolute path, but does NOT resolve symlinks in its argument
# os.path.dirname(os.path.abspath( __file__ ))

# Returns the directory in which the code file is stored
# Will first resolve any symbolic links in the path, and then return the absolute path.
# os.path.dirname(os.path.realpath(__file__))

# Returns the directory in which the code file is stored
# os.path.dirname(__file__)

# Returns the full path to the code file
# __file__

# Defaults to $PWD in your env. It's not where the script is located but where you were when you executed the script.
# os.getcwd()

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
        wire_path1, wire_path2 = [i.split(',') for i in f.readlines()]

        # Clean up newline in last element
        wire_path1[-1] = wire_path1[-1].strip()
        wire_path2[-1] = wire_path2[-1].strip()

        grid_path1 = grid_run(wire_path1)
        grid_path2 = grid_run(wire_path2)

        distance_to_collision(grid_path1, grid_path2)


def grid_run(route):
    # Old list that was too slow
    # List for the final route_path
    #route_path = []

    # Set for the final route_path
    route_path = set()

    # Variables for x/y axis
    x_axis, y_axis = 0, 0

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
            # i indicates each step needed to be taken in the grid on the x or y axis

            # To get the direction, take the route element (R990)and filter out the first letter for direction
            # R/L/U/D, take this letter as the key for the movement dictionary and save the value in offset (ex "1,0")
            # Offset will then have a value such as [1, 0]
            offset = movement[element[0]]

            # Take the offset ex [1, 0] and for the first element in the offset list save the value in the x axis.
            # For the second element in the list save the value in the y axis
            # Add the offset value so that the route moves trough the x and y axis grid, For route element R990 add
            # 990 steps to the x-axis
            x_axis += offset[0]
            y_axis += offset[1]

            # OLD LIST, was too slow
            # In route path list append tuple of x and y coordinates for each step so we can track each single step
            # that the wire takes in the grid. So for R990, first element is 1,0 next 2,0 next 3,0 and so on
            # Last element in route_path list will have the final grid coordinate for the wire
            #route_path.append((x_axis, y_axis))

            route_path.add((x_axis,y_axis))

    # Return the whole list with every single coordinate that the wire has taken
    return route_path

def distance_to_collision(route1, route2):

# Tried with a list, but to slow
#    for i, r_i in enumerate(route1):

#        for j, r_j in enumerate(route2):

#            if r_i == r_j:
#                print("collision")


    collisions = route1 & route2

    print(len(collisions))



if __name__ == "__main__":
    main()
