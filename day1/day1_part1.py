import os

def main():
    # Get current dir and append file name, so that the script can be run anywhere as long as the input file is in the
    # same dir
    file_path = os.getcwd() + '/input'

    # Open the file in read only
    module_mass_file = open(file_path, 'r')

    # Read line by line into a list
    module_mass = (module_mass_file.readlines())

    # Create a list for ints
    module_mass_int = []

    # Loop through module_mass list and convert to int in list module_mass_int
    for var in module_mass:
        module_mass_int.append(int(var))

    # Create a list for ints that holds the fuel requirement for each module mass element
    fuel_req = []

    # Loop through each value in list and for the value, divide by three, round down, and subtract 2 to get the fuel req
    for var in module_mass_int:
        fuel_req.append(int(var // 3) - 2)

    # Print the total sum of the fuel_req list
    print("Fuel needed for module mass:",sum(fuel_req))

# Only run main if executed directly
if __name__ == "__main__":
    main()