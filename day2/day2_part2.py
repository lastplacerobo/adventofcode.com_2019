import os

# Constants, cmd+alt+c, cmd,alt,v for variables
# Use refactor for name change of variable
FINISH = 99
MULTIPLY = 2
ADDITION = 1


def main():
    # Get current dir and append file name, so that the script can be run anywhere as long as the input file is in the
    # same dir
    file_path = os.getcwd() + '/input'

    # Open the file in read only
    file_input = open(file_path, 'r')

    # Read line into list and split the string into each index
    intcodes = (file_input.read())

    intcodes = intcodes.split(',')

    # Convert string list into int
    intcodes = [int(x) for x in intcodes]

    # you need to determine what pair of inputs produces the output 19690720.
    # The inputs should still be provided to the program by replacing the values
    # at addresses 1 and 2, just like before. In this program, the value placed
    # in address 1 is called the noun, and the value placed in address 2 is called the verb.
    # Each of the two input values will be between 0 and 99, inclusive.

    # Run trough noun and verb up to
    for noun in range(100):

        # Trying with taking the length of the list (int) and making a range of it.
        # Cannot just run len, since it just produces an int, and "for in" requires a list or range
        for verb in range((len(intcodes))):

            # Make a shallow copy of the original list to work with
            mutable_intcodes = intcodes.copy()

            # Loop through the list with step 4 to get the opcode
            for i in range(0, len(mutable_intcodes), 4):

                mutable_intcodes[1] = noun
                mutable_intcodes[2] = verb

                # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
                # The three integers immediately after the opcode tell you these three positions - the first two
                # indicate the positions from which you should read the input values, and the third indicates
                # the position at which the output should be stored.
                opcode = mutable_intcodes[i]
                pos_store = mutable_intcodes[i + 3]
                read_pos1 = mutable_intcodes[i + 1]
                read_pos2 = mutable_intcodes[i + 2]

                if opcode == ADDITION:

                    mutable_intcodes[pos_store] = mutable_intcodes[read_pos1] + mutable_intcodes[read_pos2]

                # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
                # Again, the three integers after the opcode indicate where the inputs and outputs are, not their values
                elif opcode == MULTIPLY:

                    mutable_intcodes[pos_store] = mutable_intcodes[read_pos1] * mutable_intcodes[read_pos2]

                # Opcode 99 means that the program is finished and should immediately halt
                elif opcode == FINISH:
                    break

                else:
                    raise Exception('Opcode should be 1/2/99. The Opcode value was:{}'.format(opcode))

            # If we find our value print it and exit
            if mutable_intcodes[0] == 19690720:
                print(100 * noun + verb)
                exit()


# Only run main if executed directly
if __name__ == "__main__":
    main()
