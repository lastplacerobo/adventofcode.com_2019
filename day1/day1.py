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

    # Create a variable for ints that holds the total extra fuel requirement for the fuel mass
    extra_fuel = 0

    # For each index of fuel, get the needed fuel for that fuel mass
    for var in fuel_req:
        extra_fuel += get_extra_fuel_mass(var)

    # Print the total sum of the extra_fuel req
    print("Fuel needed for fuel mass:",extra_fuel)

    # Print the total fuel needed
    print("Total fuel needed:",(sum(fuel_req)+extra_fuel))

# Calculate extra fuel for the fuel mass. Divide by three, round down, and subtract 2.
# Do so until you reach zero or negative for each fuel mass index.
# Function takes argument and calculates the extra fuel needed for that fuel mass.
# As long as fuel_mass is above 0 we will take fuel_mass and calculate the needed fuel for that mass. We will
# overwrite the current fuel_mass with the new fuel to be able to calculate the fuel for the new fuel mass.
# When the condition is done extra_fuel will hold all the fuel needed for the extra fuel mass.
def get_extra_fuel_mass(fuel_mass):
    extra_fuel = 0
    while fuel_mass > 0:
        fuel = fuel_mass // 3 - 2
        fuel_mass = fuel
        if fuel > 0:
            extra_fuel += fuel

    return extra_fuel

# Only run main if executed directly
if __name__ == "__main__":
    main()