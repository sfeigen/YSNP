import string

def generate():
    return "talking to password_generator"

# complicated test string to test
test_str = "! a1"

# test method to check for multipliers
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
            
def password_value(test_str):
    return len(test_str) * multiplier(test_str)
    