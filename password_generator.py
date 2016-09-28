import string

def generate():
    return "talking to password_generator"

# complicated test string to test
test_str = "! a1"

# helper method to check for multipliers
def multiplier(test_str):
    alpha, number, whitespace, special = False, False, False, False
    for i in test_str:
        if i in string.ascii_letters:
            alpha = True
        if i in string.digits:
            number = True
        if i in string.whitespace:
            whitespace = True
        if i in string.punctuation:
            special = True
    return alpha + number + whitespace + special

# check value of a given string            
def pass_val(test_str):
    return len(test_str) * multiplier(test_str)

def modifier(test_str):
    #regex to figure out if multiplier can be upgraded
    
if pass_val(test_str) >= 50:
    return test_str

if pass_val(test_str) < 50 and if pass_val > 10:
    modifier(test_str)
    return test_str

if pass_val(test_str) < 10:
    return test_str = "This shall not pass... try a strong password."