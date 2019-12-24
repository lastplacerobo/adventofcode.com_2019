import os


def main():
    # Get current dir and append file name, so that the script can be run anywhere as long as the input file is in the
    # same dir
    file_path = os.getcwd() + '/input'

    # Open the file in read only
    file_input = open(file_path, 'r')

    # Read line into list and split the string into each index
    intcode_list = (file_input.read())

    intcode_list = intcode_list.split(',')

    # Convert string list into int
    intcode_list = [int(x) for x in intcode_list]


# Only run main if executed directly
if __name__ == "__main__":
    main()
