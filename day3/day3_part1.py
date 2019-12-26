import os

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


        print(wire_path2)


if __name__ == "__main__":
    main()