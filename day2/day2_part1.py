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

    # Replace position 1 with the value 12 and replace position 2 with the value 2.
    intcode_list[1] = 12
    intcode_list[2] = 2

    # Loop through the list with step 4 to get the opcode
    for i in range(0,len(intcode_list),4):

        # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
        # The three integers immediately after the opcode tell you these three positions - the first two
        # indicate the positions from which you should read the input values, and the third indicates
        # the position at which the output should be stored.
        if intcode_list[i] == 1:

            intcode_list[intcode_list[i+3]] = intcode_list[intcode_list[i+1]] + intcode_list[intcode_list[i+2]]

        # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
        # Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
        elif intcode_list[i] == 2:

            intcode_list[intcode_list[i + 3]] = intcode_list[intcode_list[i + 1]] * intcode_list[intcode_list[i + 2]]

        elif intcode_list[i] == 99:
            break

        else:
            raise Exception('Opcode should be 1/2/99. The Opcode value was:{}'.format(intcode_list[i]))


    # The value that is left at position 0 after the program halts
    print(intcode_list[0])




# Only run main if executed directly
if __name__ == "__main__":
    main()
