

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


pass_range = list(range(146810,612564))

mega_list = []

for i in pass_range:

    invid_pass_range = []

    for str_digit in str(i):
        invid_pass_range.append(int(str_digit))

    mega_list.append(tuple(invid_pass_range))

print(mega_list[0][0])

#print(type(pass_range))

#print(pass_range[-1])
    #genererea alla nummer, stryk sedan en punkt i taget
    # ta då bort de som ej följer regler
