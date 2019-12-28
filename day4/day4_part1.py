

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

for i in range(146810,612564):
    print(i)
