from random import choice
import re
import string

rand_lower = choice(string.ascii_lowercase)
rand_upper = choice(string.ascii_uppercase)
rand_num = choice(string.digits)
rand_whitespace = choice(string.whitespace)
rand_special = choice(string.punctuation)

print(rand_lower, rand_upper, rand_num, rand_whitespace, rand_special)

# complicated test string to test
test_str = "immastring235235morestring"
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

#given range 11-49, try to beef up PW
def modifier(test_str):
    #regex to figure out if multiplier can be upgraded
    return test_str

def value_router(test_str):
    if pass_val(test_str) >= 50:
        print("Pass!")
        return test_str

    if pass_val(test_str) < 50 and pass_val(test_str) > 10:
        print("Needs some work!")
        modifier(test_str)
        return test_str

    if pass_val(test_str) <= 10:
        test_str = "This shall not pass... try a stronger password."
        return test_str