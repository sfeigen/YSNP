from random import choice
import re
import string

rand_lower = choice(string.ascii_lowercase)
rand_alpha = choice(string.ascii_letters)
rand_num = choice(string.digits)
rand_whitespace = choice(string.whitespace)
rand_special = choice(string.punctuation)

# complicated test string to test
test_str = "immastring235!s!235morestring"
test_str = re.sub(r'[a-z][a-z]*[a-z][a-z]', rand_lower, test_str)

# helper method to check for multipliers
def multiplier(test_str):
    alpha_count, number_count, whitespace_count, special_count = 0, 0, 0, 0
    alpha, number, whitespace, special = False, False, False, False
    for i in test_str:
        if i in string.ascii_letters:
            alpha = True
            alpha_count += 1
        if i in string.digits:
            number = True
            number_count += 1
        if i in string.whitespace:
            whitespace = True
            whitespace_count += 1
        if i in string.punctuation:
            special = True
            special_count += 1

    multiplier = alpha + number + whitespace + special
    count = [alpha_count, number_count, whitespace_count, special_count]
    return multiplier, count

# check value of a given string            
def pass_val(test_str):
    return len(test_str) * multiplier(test_str)[0]

#given range 11-49, try to beef up PW if redundant
def modifier(test_str):
    print("Modifying string...")
    #alpha = [0], number = [1], whitespace = [2], special = [3]
    count = multiplier(test_str)[1]

    while pass_val(test_str) < 50:
        #number redundant, swap
        if count[1] >= 2 and count[0] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'[0-9]', rand_alpha, test_str, 1)[0]
        if count[1] >= 2 and count[2] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'[0-9]', rand_whitespace, test_str, 1)[0]
        if count[1] >= 2 and count[3] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'[0-9]', rand_special, test_str, 1)[0]

        #special redundant, swap
        if count[3] >= 2 and count[0] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_alpha, test_str, 1)[0]
        if count[3] >= 2 and count[1] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_num, test_str, 1)[0]
        if count[3] >= 2 and count[2] == 0 and pass_val(test_str) < 50:
            test_str = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_whitespace, test_str, 1)[0]

        if pass_val(test_str) < 50 and len(test_str) < 13:
            difference = 13 - len(test_str)
            test_str = test_str + "1*a " + (difference*choice(string.digits))
        
        print("Modified string: ", test_str, pass_val(test_str))
    return test_str

def value_router(test_str):
    if pass_val(test_str) >= 50:
        print("Pass!")
        # test_str = test_str + " <- passed with a score of: ", pass_val(test_str)
        return test_str

    if pass_val(test_str) < 50 and pass_val(test_str) > 10:
        test_str = modifier(test_str)
        # test_str = test_str + " <- modified password with a score of: ", pass_val(test_str)
        return test_str

    if pass_val(test_str) <= 10:
        # test_str = test_str + " <- this shall not pass... the value is: ", pass_val(test_str)
        return test_str