import os

def main():

    # Get current dir and append file name, so that the script can be run anywhere as long as the input file is in the
    # same dir
    file_path = os.getcwd() + '/input'

    # Open the file in read only
    file_input = open(file_path, 'r')

    # Read line by line into a list
    intcode_list = (file_input.readlines())

    intcode_list = intcode_list.split(',')

    # Convert list to int
#    for var in intcode_list:
#       intcode_list.append(int(var))

#    print(type(intcode_list))
#    print(type(intcode_list[0]))




# Only run main if executed directly
if __name__ == "__main__":
    main()
