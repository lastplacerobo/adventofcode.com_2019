import os


def main():
    dir = os.path.dirname(__file__)

    with open(os.path.join(dir, "input")) as f:
        # Iterate trough input file, split on comma, save in two lists
        wire_path1, wire_path2 = [i.split(',') for i in f.readlines()]

        # Clean up newline in last element
        wire_path1[-1] = wire_path1[-1].strip()
        wire_path2[-1] = wire_path2[-1].strip()

        grid_path1 = grid_run(wire_path1)
        grid_path2 = grid_run(wire_path2)

        distance_to_collision(grid_path1, grid_path2)


def grid_run(route):
    # Dic for the final route_path
    route_path = {}

    # Variables for x/y axis, and steps taken
    x_axis, y_axis, steps = 0, 0, 0

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

            # Add to variable steps so we know how many steps it has been from the start
            steps += 1

            # In route path dic add tuple of x and y coordinates for each step so we can track each single step
            # that the wire takes in the grid. So for R990, first key is 1,0 next 2,0 next 3,0 and so on
            # Last key in route_path dic will have the final grid coordinate for the wire. For each key the value is
            # the number of steps needed to be there from 0,0
            route_path[(x_axis, y_axis)] = steps

    # Return the whole set with every single coordinate that the wire has taken
    return route_path


def distance_to_collision(route1, route2):
    # Find the smallest distance in steps from the central port (0, 0) to the intersection(collision)

    # Compare the two dic, since the elements are hashed we can compare the keys. The ones that are identical are the
    # the same grid coordinates. Save as list so we have indexes to reference
    collisions = list(route1.keys() & route2.keys())

    # Go trough the collisions list elements of all x and y coordinates that the wires has crossed each other
    # Use the collision list (coordinates where wires has crossed) and use as key to get the value of steps
    # in dic route1 and route2. Append these step values in two lists, step1 and step2

    step1 = []
    step2 = []

    for i, r_i in enumerate(collisions):
        step1.append(route1.get(collisions[i]))
        step2.append(route2.get(collisions[i]))

    sum_step = []

    # step1 and step2 has the steps taken too reach the collision(intersection) for each wire
    # Go trough each step value and sum the steps together for each wire
    # sum_step will contain a list of a sum of the steps taken for both wires to each collision

    for i, r_i in enumerate(step1):
        sum_step.append((step1[i] + step2[i]))

    # To answer: "What is the fewest combined steps the wires must take to reach an intersection?"
    # Take the minimum value from the list sum_step
    print(min(sum_step))


if __name__ == "__main__":
    main()
