

# Password is 6 digits
# Password in range(146810,612564)
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease;
# they only ever increase or stay the same (like 111123 or 135679).

# The following are true:
#    111111 meets these criteria (double 11, never decreases).
#    223450 does not meet these criteria (decreasing pair of digits 50).
#    123789 does not meet these criteria (no double).

# How many different passwords within the range given in your puzzle input meet these criteria?

# Input range
pass_range = list(range(146810,612564))

# Store the pass range with each character as a individual element
pass_list = []

# Split up the password range element to individual tuples
for i in pass_range:

    # Store
    id_pass_range = []

    # For each individual character go trough and save in list as a separate element
    for str_digit in str(i):
        id_pass_range.append(int(str_digit))

    # Save the list inside a list - listinception
    pass_list.append(id_pass_range)


#for h in len(pass_range):
#    for k in len(h):
#        print(pass_list[h][k])

#print(pass_range[-1])
    #genererea alla nummer, stryk sedan en punkt i taget
    # ta då bort de som ej följer regler

