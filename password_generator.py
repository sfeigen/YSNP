from random import choice
import re
import string

rand_lower = choice(string.ascii_lowercase)
rand_alpha = choice(string.ascii_letters)
rand_num = choice(string.digits)
rand_whitespace = choice(string.whitespace)
rand_special = choice(string.punctuation)

# complicated test string to test
password = "immastring235!s!235morestring"
password = re.sub(r'[a-z][a-z]*[a-z][a-z]', rand_lower, password)

# helper method to check for multipliers
def multiplier(password):
    #reset for update function
    multiplier = 0

    alpha_count, number_count, whitespace_count, special_count = 0, 0, 0, 0
    alpha, number, whitespace, special = False, False, False, False
    for i in password:
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
def pass_val(password):
    return len(password) * multiplier(password)[0]

#given range 11-49, try to beef up PW if redundant
def modifier(password):
    print("Modifying string...")
    #alpha = [0], number = [1], whitespace = [2], special = [3]
    count = multiplier(password)[1]

    while pass_val(password) < 50:
        #number redundant, swap
        if count[1] >= 2 and count[0] == 0 and pass_val(password) < 50:
            password = re.subn(r'[0-9]', rand_alpha, password, 1)[0]
        if count[1] >= 2 and count[2] == 0 and pass_val(password) < 50:
            password = re.subn(r'[0-9]', rand_whitespace, password, 1)[0]
        if count[1] >= 2 and count[3] == 0 and pass_val(password) < 50:
            password = re.subn(r'[0-9]', rand_special, password, 1)[0]

        #special redundant, swap
        if count[3] >= 2 and count[0] == 0 and pass_val(password) < 50:
            password = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_alpha, password, 1)[0]
        if count[3] >= 2 and count[1] == 0 and pass_val(password) < 50:
            password = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_num, password, 1)[0]
        if count[3] >= 2 and count[2] == 0 and pass_val(password) < 50:
            password = re.subn(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', rand_whitespace, password, 1)[0]

        if pass_val(password) < 50 and len(password) < 13:
            difference = 13 - len(password)
            password = password + "1*a " + (difference*choice(string.digits))
        
        print("Modified string: ", password, pass_val(password))
        return password

def value_router(password):
    if pass_val(password) >= 50:
        print("Pass!")
        return password

    if pass_val(password) < 50 and pass_val(password) > 10:
        password = modifier(password)
        return password

    if pass_val(password) <= 10:
        return password